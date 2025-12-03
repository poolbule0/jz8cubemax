#!/usr/bin/env python
# -*- coding: gbk -*-
"""
pwm.c 代码生成器
生成PWM功能代码文件
"""

from .base_generator import BaseGenerator


class PWMGenerator(BaseGenerator):
    """pwm.c 代码生成器"""
    
    def generate(self) -> str:
        """生成PWM代码"""
        # 根据芯片类型选择不同的生成方法
        if self.chip_name == "JZ8P1521":
            return self._generate_1521()
        else:
            return self._generate_generic()
    
    def _generate_1521(self) -> str:
        """生成JZ8P1521的PWM代码"""
        code = []
        code.append("#include \"pwm.h\"")
        code.append("")
        
        cfg_pwm = self.config_data.get("pwm", {})
        
        # JZ8P1521有3路PWM（PWM1, PWM2, PWM3），共周期8位
        # 函数名使用fw_pwm1Init, fw_pwm2Init, fw_pwm3Init（与main.c调用一致）
        channel_sequence = [
            ("PWM1", "fw_pwm1Init", 0x10),  # Bit4: PWM1EN
            ("PWM2", "fw_pwm2Init", 0x20),  # Bit5: PWM2EN
            ("PWM3", "fw_pwm3Init", 0x40),  # Bit6: PWM3EN
        ]
        
        first_function = True
        for ch_name, func_name, pwm_enable_bit in channel_sequence:
            pwm_cfg = cfg_pwm.get(ch_name, {})
            if not pwm_cfg.get("enabled"):
                continue
            
            if not first_function:
                code.append("")
            first_function = False
            
            if self._should_include_comments():
                code.append("/******************************************")
                code.append(" * ")
                code.append(f" * 函数 :  {func_name}()")
                code.append(f" * 功能 : {ch_name} 初始化")
                code.append(" *")
                code.append("*******************************************/")
            code.append(f"void {func_name}()")
            code.append("{")
            
            # 使用按位或操作设置PWMCON（与示例项目一致）
            self._add_comment(code, "    /********** 选择PWM模块时钟 *************/")
            code.append("\tPWMCON |= 0x80;")
            code.append("\tPWMCON |= D_PWM_DIV_SLCT;")
            code.append(f"\tPWMCON |= 0x{pwm_enable_bit:02X};")
            code.append("")
            
            # CPUCON寄存器配置（与示例项目一致）
            code.append("\tCPUCON = 0; //bit7:IPWM1-PWM互补输出 1：pwm取反 bit6:时钟源选择1：系统时钟0：指令时钟 bit4:PWMWE-PWM 唤醒 1:PWM 唤醒使能，可唤?芽障心Ｊ?")
            code.append("")
            
            # PRD寄存器（周期，8位，0-255）
            period = int(pwm_cfg.get("period", 100)) & 0xFF
            self._add_code_with_comment(code, f"\tPRD = {period};", "PWM周期")
            code.append("")
            
            # PDC寄存器（占空比，8位，0-255）
            duty = int(pwm_cfg.get("duty", 0))
            if duty <= 100:
                # 如果是百分比，转换为0-255的值
                duty = (period * duty) // 100
            duty = duty & 0xFF
            
            if ch_name == "PWM1":
                self._add_code_with_comment(code, f"\tPDC1 = {duty};", "pwmDUTY")
            elif ch_name == "PWM2":
                self._add_code_with_comment(code, f"\tPDC2 = {duty};", "pwmDUTY")
            else:  # PWM3
                self._add_code_with_comment(code, f"\tPDC3 = {duty};", "pwmDUTY")
            code.append("")
            
            # 中断配置（示例代码中关闭PWM中断，只使能TCC中断）
            self._add_code_with_comment(code, f"\tIOCP_W(IMR,0X01);", "TCC中断 关闭pwm中断")
            code.append("")
            
            # 清除中断标志位（清除T1IF，Bit3）
            self._add_code_with_comment(code, f"\tISR = 0xf7;", "清除溢出标志位")
            
            code.append("}")
        
        if first_function:
            self._add_comment(code, "当前未启用任何 PWM 通道")
        code.append("")
        return "\n".join(code)
    
    def _generate_generic(self) -> str:
        """生成通用芯片的PWM代码（保留原有逻辑）"""
        cfg_pwm = self.config_data.get("pwm", {})
        
        def _duty_to_counts(period_val: int, duty_percent: int) -> int:
            """将占空比百分比转换成计数值（0-1023）"""
            if period_val <= 0:
                return 0
            duty_percent = max(0, min(100, duty_percent))
            duty_counts = (period_val * duty_percent) // 100
            return min(duty_counts, 0x3FF)

        def _pwm_clock_line(channel: str) -> str:
            clock = cfg_pwm.get(channel, {}).get("clock_source", "instruction")
            if self._should_include_comments():
                if clock == "system":
                    return "\tPWMCON |= 0x40;\t\t//PWM时钟 = 系统周期"
                return "\tPWMCON |= 0x00;\t\t//PWM时钟 = 指令周期"
            else:
                if clock == "system":
                    return "\tPWMCON |= 0x40;"
                return "\tPWMCON |= 0x00;"

        code = []
        code.append("#include \"pwm.h\"")
        code.append("")
        
        channel_sequence = [
            ("PWM1", "fw_pwm1Init", "TC1(PWM1/PWM3)", "TC1CON = 0x88;\t\t//TC1控制寄存器 (TC1EN=1, PWM1E=1)", "PWM1"),
            ("PWM2", "fw_pwm2Init", "TC2(PWM2/PWM4)", "TC2CON |= 0x88;\t\t//TC2控制寄存器 (TC2EN=1, PWM2E=1)", "PWM2"),
            ("PWM3", "fw_pwm3Init", "TC1(PWM1/PWM3)", "TC1CON = 0xA0;\t\t//TC1控制寄存器 (TC1EN=1, PWM3E=1)", "PWM3"),
            ("PWM4", "fw_pwm4Init", "TC2(PWM2/PWM4)", "TC2CON |= 0xA0;\t\t//TC2控制寄存器 (TC2EN=1, PWM4E=1)", "PWM4"),
        ]

        first_function = True
        for ch_name, func_name, section_title, tc_con_line, pwm_label in channel_sequence:
            pwm_cfg = self.config_data.get("pwm", {}).get(ch_name, {})
            if not pwm_cfg.get("enabled"):
                continue

            if not first_function:
                code.append("")
            first_function = False

            if self._should_include_comments():
                code.append("/******************************************")
                code.append(" * ")
                code.append(f" * 函数 :  {func_name}()")
                code.append(f" *  * 功能 : {pwm_label} 初始化")
                code.append(" *")
                code.append("*******************************************/")
            code.append(f"void {func_name}()")
            code.append("{")
            code.append(_pwm_clock_line(ch_name))

            period = int(pwm_cfg.get("period", 100)) & 0x3FF
            duty = _duty_to_counts(period, int(pwm_cfg.get("duty", 0)))
            prd_low = period & 0xFF
            prd_high = (period >> 8) & 0x03
            duty_low = duty & 0xFF
            duty_high = (duty >> 8) & 0x03

            if ch_name in ("PWM1", "PWM2"):
                tc_prdth = (prd_high << 6) | (duty_high << 2)
            else:
                tc_prdth = (prd_high << 6)

            self._add_comment(code, f"==========={section_title}初始化============")
            tc_line_clean = tc_con_line.split("//")[0].rstrip() if not self._should_include_comments() else tc_con_line
            code.append(f"\t{tc_line_clean}")

            if ch_name in ("PWM1", "PWM2"):
                if ch_name == "PWM1":
                    self._add_code_with_comment(code, f"\tTC1PRDTH = 0x{tc_prdth:02X};", "TC1周期高2位 / PWM1占空比高2位")
                    self._add_code_with_comment(code, f"\tTC1PRDL = 0x{prd_low:02X};", "TC1（PWM1、PWM3）周期低8位")
                    self._add_code_with_comment(code, f"\tPWM1DTL = 0x{duty_low:02X};", "PWM1占空比低8位")
                else:
                    self._add_code_with_comment(code, f"\tTC2PRDTH = 0x{tc_prdth:02X};", "TC2周期高2位 / PWM2占空比高2位")
                    self._add_code_with_comment(code, f"\tTC2PRDL = 0x{prd_low:02X};", "TC2（PWM2/PWM4）周期低8位")
                    self._add_code_with_comment(code, f"\tPWM2DTL = 0x{duty_low:02X};", "PWM2占空比低位寄存器")
            elif ch_name == "PWM3":
                self._add_code_with_comment(code, f"\tTC1PRDTH = 0x{tc_prdth:02X};", "TC1（PWM1、PWM3）周期高2位")
                self._add_code_with_comment(code, f"\tTC1PRDL = 0x{prd_low:02X};", "TC1（PWM1、PWM3）周期低8位")
                code.append("")
                self._add_code_with_comment(code, f"\tPWM3DTH = 0x{duty_high:02X};", "PWM3占空比高位寄存器")
                self._add_code_with_comment(code, f"\tPWM3DTL = 0x{duty_low:02X};", "PWM3占空比低位寄存器")
            else:  # PWM4
                code.append("")
                self._add_code_with_comment(code, f"\tTC2PRDTH = 0x{tc_prdth:02X};", "TC2周期高2位")
                self._add_code_with_comment(code, f"\tTC2PRDL = 0x{prd_low:02X};", "TC2（PWM2/PWM4）周期低8位")
                code.append("")
                self._add_code_with_comment(code, f"\tPWM4DTH = 0x{duty_high:02X};", "PWM4占空比高位寄存器")
                self._add_code_with_comment(code, f"\tPWM4DTL = 0x{duty_low:02X};", "PWM4占空比低位寄存器")

            map_pin = pwm_cfg.get("mapping", "P60" if ch_name == "PWM1" else
                                  "P61" if ch_name == "PWM2" else
                                  "P62" if ch_name == "PWM3" else "P63")

            if ch_name == "PWM1":
                code.append("")
                if map_pin == "P52":
                    self._add_code_with_comment(code, "\tPWMIS |= 0x01;", "PWM1 映射到 P52")
                else:
                    self._add_code_with_comment(code, "\tPWMIS &= ~0x01;", "PWM1 映射到 P60")
            elif ch_name == "PWM2":
                code.append("")
                if map_pin == "P53":
                    self._add_code_with_comment(code, "\tPWMIS |= 0x04;", "PWM2 映射到 P53")
                else:
                    self._add_code_with_comment(code, "\tPWMIS &= ~0x04;", "PWM2 映射到 P61")
            elif ch_name == "PWM3":
                code.append("")
                if map_pin == "P54":
                    self._add_code_with_comment(code, "\tPWMIS |= 0x10;", "PWM3 映射到 P54")
                else:
                    self._add_code_with_comment(code, "\tPWMIS &= ~0x10;", "PWM3 映射到 P62")
            else:
                code.append("")
                if map_pin == "P55":
                    self._add_code_with_comment(code, "\tPWMIS |= 0x40;", "PWM4 映射到 P55")
                else:
                    self._add_code_with_comment(code, "\tPWMIS &= ~0x40;", "PWM4 映射到 P63")
                code.append("")
                self._add_code_with_comment(code, "\tDEADCON |= 0x20;", "死区控制寄存器（示例默认开启 PWM2/4 死区）")

            code.append("}")

        if first_function:
            self._add_comment(code, "当前未启用任何 PWM 通道")
        code.append("")
        return "\n".join(code)

