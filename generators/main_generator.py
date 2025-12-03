#!/usr/bin/env python
# -*- coding: gbk -*-
"""
main.c 代码生成器
生成主程序代码文件
"""

from .base_generator import BaseGenerator


class MainGenerator(BaseGenerator):
    """main.c 代码生成器"""
    
    def generate(self) -> str:
        """生成主程序代码"""
        code = []
        cfg_isr = self.config_data.get("isr", {})
        t10_flag = cfg_isr.get("time_10ms_flag", "Time_10ms")
        
        # 根据芯片类型使用不同的头文件包含
        if self._is_chip_1521():
            code.append("#include \"main.h\"")
        else:
            code.append(f"#include \"{self.header_file_name}\"")
            code.append("#include \"main.h\"")
            code.append("#include \"init.h\"")
            code.append("#include \"type.h\"")
            if self.config_data.get("sleep", {}).get("enabled"):
                code.append("#include \"sleep.h\"")
            if self.config_data.get("adc", {}).get("enabled", False):
                code.append("#include \"ADC.H\"")
        code.append("")
        
        # 根据芯片类型使用不同的变量名
        if self._is_chip_1521():
            code.append("SYS_FlgBitClass\tU_Flage;")
        else:
            code.append("SYS_FlgBitClass U_Flage1;")
        code.append("uint8_t r_g_workMod;")
        code.append("")
        
        code.append("void main()")
        code.append("{")
        
        # 根据芯片类型使用不同的函数调用
        if self._is_chip_1521():
            self._add_code_with_comment(code, "\tfw_clrRam();", "清RAM")
            self._add_code_with_comment(code, "\tfw_gpioInit();", "端口初始化")
            if "TCC" in self.config_data.get("timer", {}) and self.config_data["timer"]["TCC"]["enabled"]:
                self._add_code_with_comment(code, "\tfw_tc0Init();", "定时器初始化")
            # PWM初始化（1521使用fw_pwm1Init, fw_pwm2Init, fw_pwm3Init）
            if self.config_data["pwm"].get("PWM1", {}).get("enabled"):
                code.append("\tfw_pwm1Init();")
            if self.config_data["pwm"].get("PWM2", {}).get("enabled"):
                code.append("\tfw_pwm2Init();")
            if self.config_data["pwm"].get("PWM3", {}).get("enabled"):
                code.append("\tfw_pwm3Init();")
            code.append("")
            self._add_code_with_comment(code, "\tEI();", "开启中断")
        else:
            code.append("\tfile_clrRam();")
            self._add_code_with_comment(code, "\tfile_init();", "初始化")
            if "TC0" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC0"]["enabled"]:
                code.append("\tfile_tc0_Init();")
            if "TC1" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC1"]["enabled"]:
                code.append("\tfile_tc1_Init();")
            if "TC2" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC2"]["enabled"]:
                code.append("\tfile_tc2_Init();")
            if self.config_data.get("adc", {}).get("enabled", False):
                code.append("\tfile_adc_Init();")
            pwm_enabled = any(self.config_data["pwm"][pwm]["enabled"] for pwm in ["PWM1", "PWM2", "PWM3", "PWM4"])
            if pwm_enabled:
                code.append("\tfile_pwm_Init();")
            code.append("\tei();")
        
        code.append("\twhile(1)")
        code.append("\t{")
        
        if self._is_chip_1521():
            code.append(f"\t\tif ({t10_flag})")
            code.append("\t\t{")
            code.append(f"\t\t\t{t10_flag} = DISABLE;")
            if self.config_data.get("sleep", {}).get("enabled"):
                code.append("\t\t\tfw_sleepEvent();")
            self._add_comment(code, "\t\t\t// 用户代码区域")
            code.append("\t\t")
            code.append("\t\t}")
        else:
            self._add_comment(code, "\t\t// 用户代码区域")
            code.append("")
            t200_flag = cfg_isr.get("time_200us_flag", "Time_200us")
            code.append(f"\t\tif ({t200_flag})")
            code.append("\t\t{")
            code.append(f"\t\t\t{t200_flag} = 0;")
            self._add_comment(code, "\t\t\t// 在这里处理 200us 周期任务")
            code.append("\t\t}")
            code.append("")
            code.append(f"\t\tif ({t10_flag})")
            code.append("\t\t{")
            code.append(f"\t\t\t{t10_flag} = 0;")
            self._add_comment(code, "\t\t\t// 在这里处理 10ms 周期任务")
            if self.config_data.get("sleep", {}).get("enabled"):
                code.append("\t\t\tsleep_scan();")
            code.append("\t\t}")
        
        code.append("\t}")
        code.append("}")
        code.append("")
        
        return "\n".join(code)

