#!/usr/bin/env python
# -*- coding: gbk -*-
"""
init.c 代码生成器
生成初始化代码文件
"""

from typing import List
from .base_generator import BaseGenerator
from utils.register_calc import calculate_port_control, calculate_port_pull
from utils.register_calc import compute_wdtcon_value, compute_inte0_value, compute_inte1_value


class InitGenerator(BaseGenerator):
    """init.c 代码生成器"""
    
    def generate(self) -> str:
        """生成初始化代码"""
        code = []
        
        # 根据芯片类型使用不同的头文件包含
        if self._is_chip_1521():
            code.append("#include \"user.h\"")
        else:
            code.append("#include \"init.h\"")
            code.append("#include \"type.h\"")
            code.append("#include \"main.h\"")
            code.append(f"#include \"{self.header_file_name}\"")
        code.append("")
        
        # 生成RAM清零函数
        if self._is_chip_1521():
            self._add_comment(code, "//===================================//")
            self._add_comment(code, "//初始化RAM:10H~3FH")
            self._add_comment(code, "//===================================//")
            code.append("void fw_clrRam()")
        else:
            code.append("void file_clrRam(void)")
        code.append("{")
        self._add_code_with_comment(code, "\tfor(RSR=0x90;RSR<0xFF;RSR++)", "清零 BANK0 RAM  IAR-R0,RSR-R4")
        code.append("\t{IAR = 0;}")
        code.append("\t IAR = 0;")
        code.append("}")
        
        # 根据芯片类型生成不同的GPIO配置代码
        if self._is_chip_1521():
            self._add_comment(code, "//===================================//")
            self._add_comment(code, "//端口初始??")
            self._add_comment(code, "//===================================//")
            code.append("void fw_gpioInit(void)")
            code.append("{")
            code.extend(self._generate_gpio_init_1521())
            code.append("}")
            code.append("")
            
            # 生成定时器初始化代码（1521中TCC初始化在user.c中）
            if "TCC" in self.config_data.get("timer", {}) and self.config_data["timer"]["TCC"]["enabled"]:
                self._add_comment(code, "//===================================//")
                self._add_comment(code, "//TC0初始化")
                self._add_comment(code, "//===================================//")
                code.append("void fw_tc0Init()")
                code.append("{")
                code.extend(self._generate_tcc_init_code())
                code.append("}")
        else:
            self._add_comment(code, "===================================//")
            self._add_comment(code, "端口初始化")
            self._add_comment(code, "===================================//")
            code.append("void file_init(void)")
            code.append("{")
            self._add_comment(code, "===========端口初始化=============")
            code.extend(self._generate_gpio_init_2615())
            
            # 中断配置
            code.extend(self._generate_interrupt_init_2615())
            code.append("}")
            code.append("")
            
            # 生成定时器初始化代码
            if "TC0" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC0"]["enabled"]:
                code.extend(self._generate_tc0_init_code())
            if "TC1" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC1"]["enabled"]:
                code.extend(self._generate_tc1_init_code())
            if "TC2" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC2"]["enabled"]:
                code.extend(self._generate_tc2_init_code())
            
            # 生成ADC初始化代码（仅JZ8P2615支持）
            if self.config_data.get("adc", {}).get("enabled", False):
                code.extend(self._generate_adc_init_code())
        
        # 生成PWM初始化代码（1521的PWM在pwm.c中，不在这里）
        if not self._is_chip_1521():
            pwm_enabled = any(self.config_data["pwm"][pwm]["enabled"] for pwm in ["PWM1", "PWM2", "PWM3", "PWM4"])
            if pwm_enabled:
                code.extend(self._generate_pwm_init_code())
        
        return "\n".join(code)
    
    def _generate_gpio_init_1521(self) -> List[str]:
        """生成 JZ8P1521 的 GPIO 初始化代码"""
        code = []
        gpio_config = self.config_data["gpio"]
        
        # 计算寄存器值
        p5_direction = gpio_config["P5"]["direction"][:4]  # 只取前4位
        p6_direction = gpio_config["P6"]["direction"]
        
        p5con = calculate_port_control(p5_direction)
        p6con = calculate_port_control(p6_direction)
        
        # P5上拉（IOC9的低4位）
        p5ph = calculate_port_pull(gpio_config["P5"]["pullup"][:4])
        # P6上拉（IOCD寄存器）
        p6ph = calculate_port_pull(gpio_config["P6"]["pullup"])
        
        # P5下拉（IOCB的低4位）
        p5pd = calculate_port_pull(gpio_config["P5"]["pulldown"][:4])
        # P6下拉（IOC9的高4位和IOCB的6:4位）
        p6pd_high = calculate_port_pull(gpio_config["P6"]["pulldown"][4:8]) << 4
        p6pd_low = calculate_port_pull(gpio_config["P6"]["pulldown"][:3]) << 4
        
        # P6唤醒使能（RPAGE-RD寄存器）
        p6iwe = calculate_port_pull(gpio_config["P6"]["wakeup"], invert=True)
        
        # 使用IOCP_W宏访问IOPAGE寄存器
        # P5方向控制（IOC5/P5CR）
        self._add_code_with_comment(code, f"\tIOCP_W(P5CR, 0x{p5con:02X});", "P5口设为输出\t;0输出，1输入")
        code.append(f"\tPORT5 = 0;")
        code.append("")
        
        # P6方向控制（IOC6/P6CR）
        self._add_code_with_comment(code, f"\tIOCP_W(P6CR, 0x{p6con:02X});", "P6口设为输出\t;0输出，1输入")
        code.append(f"\tPORT6 = 0;")
        code.append("")
        
        # 端口上下拉控制（IOC9/PHDCR）
        # bit7-bit4对应P67-P64下拉;bit3-bit0对应P53-P50上拉
        ioc9_value = p6pd_high | p5ph
        self._add_code_with_comment(code, f"\tIOCP_W(PHDCR, 0x{ioc9_value:02X});", 
                                   "端口上下拉控制\t;bit7-bit4对应P67-P64下拉;bit3-bit0对应P53-P50上拉")
        
        # 端口下拉控制（IOCB/PDCR）
        # bit6-bit4对应P62-P60,bit3-bit0对应P53-P50
        iocb_value = 0x80 | p6pd_low | p5pd
        self._add_code_with_comment(code, f"\tIOCP_W(PDCR, 0x{iocb_value:02X});", 
                                   "端口下拉控制\t;bit6-bit4对应P62-P60,bit3-bit0对应P53-P50")
        
        # P6端口上拉控制（IOCD/PHCR）
        # bit7-bit0对应P67-P60
        self._add_code_with_comment(code, f"\tIOCP_W(PHCR, 0x{p6ph:02X});", 
                                   "P6端口上拉控制\t;bit7-bit0对应P67-P60,0使能，1禁止")
        code.append("")
        
        # WDT控制寄存器（IOCE/WDTCR）
        system_config = self.config_data.get("system", {})
        wdt_config = system_config.get("wdt", {})
        wdtcr_value = 0x00
        if not wdt_config.get("enabled", False):
            wdtcr_value = 0x00
        self._add_code_with_comment(code, f"\tIOCP_W(WDTCR, 0x{wdtcr_value:02X});", "WDT 使能控制寄存器")
        code.append("")
        
        # P6端口中断唤醒使能（RD寄存器/ICIECR，在RPAGE中，直接访问）
        self._add_comment(code, "-----端口变化中断唤醒------")
        self._add_code_with_comment(code, f"\tICIECR = 0x{p6iwe:02X};", "P6口状态变化唤醒使能\t;0禁止，1使能")
        code.append("")
        
        return code
    
    def _generate_gpio_init_2615(self) -> List[str]:
        """生成 JZ8P2615 的 GPIO 初始化代码"""
        code = []
        gpio_config = self.config_data["gpio"]
        
        # 计算寄存器值
        p5con = calculate_port_control(gpio_config["P5"]["direction"])
        p6con = calculate_port_control(gpio_config["P6"]["direction"])
        p5ph = calculate_port_pull(gpio_config["P5"]["pullup"])
        p6ph = calculate_port_pull(gpio_config["P6"]["pullup"])
        p5pd = calculate_port_pull(gpio_config["P5"]["pulldown"])
        p6pd = calculate_port_pull(gpio_config["P6"]["pulldown"])
        p6od = calculate_port_pull(gpio_config["P6"].get("opendrain", [0]*8), invert=True)
        p6wd = calculate_port_pull(gpio_config["P6"].get("weakdrive", [0]*8), invert=True)
        p5iwe = calculate_port_pull(gpio_config["P5"].get("wakeup", [0]*8), invert=True)
        p6iwe = calculate_port_pull(gpio_config["P6"].get("wakeup", [0]*8), invert=True)
        
        code.append(f"\tPORT5=0x00;")
        code.append(f"\tPORT6=0x00;")
        code.append("")
        self._add_code_with_comment(code, f"\tP5CON=0x{p5con:02X};", "P5端口控制\t;0输出，1输入")
        self._add_code_with_comment(code, f"\tP6CON=0x{p6con:02X};", "P6端口控制    ;0输出，1输入")
        code.append("")
        self._add_code_with_comment(code, f"\tP5PH=0x{p5ph:02X};", "P5口上拉\t\t;0使能，1禁止")
        self._add_code_with_comment(code, f"\tP6PH=0x{p6ph:02X};", "P6口上拉\t\t;0使能，1禁止")
        code.append("")
        self._add_code_with_comment(code, f"\tP5PD=0x{p5pd:02X};", "P5口下拉\t\t;0使能，1禁止")
        self._add_code_with_comment(code, f"\tP6PD=0x{p6pd:02X};", "P6口下拉\t\t;0使能，1禁止")
        code.append("")
        self._add_code_with_comment(code, f"\tP6OD=0x{p6od:02X};", "P6口开漏\t\t;0禁止，1使能")
        self._add_code_with_comment(code, f"\tP6WD=0x{p6wd:02X};", "P6口弱驱动   ;0禁止，1使能")
        code.append("")
        self._add_comment(code, "-----端口变化中断唤醒------")
        self._add_code_with_comment(code, f"\tP5IWE=0x{p5iwe:02X};", "P5口状态变化唤醒使能")
        self._add_code_with_comment(code, f"\tP6IWE=0x{p6iwe:02X};", "P6口状态变化唤醒使能")
        code.append("")
        
        return code
    
    def _generate_interrupt_init_1521(self) -> List[str]:
        """生成 JZ8P1521 的中断初始化代码"""
        code = []
        interrupt_config = self.config_data.get("interrupt", {})
        
        # JZ8P1521 使用 IOCE (WDT控制) 和 IOCF (中断使能控制)
        wdten = 0x00
        eis = 0x00
        if interrupt_config.get("EXINT", {}).get("enabled", False):
            eis = 0x40
        
        # IOCE: WDT控制及外部中断使能寄存器
        ioce_value = 0xFE  # 默认值
        wdten = 0x00
        system_config = self.config_data.get("system", {})
        wdt_config = system_config.get("wdt", {})
        if wdt_config.get("enabled", False):
            wdten = 0x80  # Bit7: WDTEN
        
        eis = 0x00
        if interrupt_config.get("EXINT", {}).get("enabled", False):
            eis = 0x40  # Bit6: EIS (P60外部中断)
        
        ioce_value = 0xFE | wdten | eis
        self._add_comment(code, " -----使能外部中断设置------")
        self._add_code_with_comment(code, f"\tIOCP_W(WDTCR, 0x{ioce_value:02X});", 
                                     "WDT控制及外部中断使能\t;Bit7=WDTEN,Bit6=EIS(P60外部中断)")
        code.append("")
        
        # IOCF: 中断使能控制寄存器（在头文件中可能叫IMR）
        iocf_value = 0x00
        if interrupt_config.get("T1_PWM", {}).get("enabled", False):
            iocf_value |= 0x08  # Bit3: T1IE
        if interrupt_config.get("EXINT", {}).get("enabled", False):
            iocf_value |= 0x04  # Bit2: EXIE
        if interrupt_config.get("PORT_CHANGE", {}).get("enabled", False):
            iocf_value |= 0x02  # Bit1: ICIE
        if interrupt_config.get("TCC", {}).get("enabled", False):
            iocf_value |= 0x01  # Bit0: TCIE
        
        self._add_code_with_comment(code, f"\tIOCP_W(IMR, 0x{iocf_value:02X});", 
                                   "中断使能控制\t;T1IE,EXIE,ICIE,TCIE")
        
        # 清中断标志位（ISR寄存器，在RPAGE中，直接访问）
        code.append("")
        self._add_code_with_comment(code, f"\tISR = 0x00;", "清中断标志位")
        code.append("")
        
        return code
    
    def _generate_interrupt_init_2615(self) -> List[str]:
        """生成 JZ8P2615 的中断初始化代码"""
        code = []
        int_config = self.config_data["interrupt"]
        wdtcon = compute_wdtcon_value(int_config)
        inte0 = compute_inte0_value(int_config)
        inte1 = compute_inte1_value(int_config)
        
        self._add_comment(code, " -----使能外部中断设置------")
        self._add_code_with_comment(code, f"\tWDTCON=0x{wdtcon:02X};", "bit6&5:P60&P53外部中断功能控制位，0:普通IO口, 1:外部中断口")
        code.append("")
        self._add_code_with_comment(code, f"\tINTE0=0x{inte0:02X};", "中断使能")
        self._add_code_with_comment(code, f"\tINTE1=0x{inte1:02X};", "周期及占空比中断")
        self._add_code_with_comment(code, f"\tINTF0=0x00;", "清中断标志位")
        code.append(f"\tINTF1=0x00;")
        code.append("")
        
        return code
    
    def _generate_tcc_init_code(self) -> List[str]:
        """生成TCC定时器初始化代码（JZ8P1521）- 只生成函数体"""
        code = []
        config = self.config_data["timer"]["TCC"]

        # CONT寄存器计算
        # Bit2-0: 预分频比（0-7对应1:2, 1:4, 1:8, 1:16, 1:32, 1:64, 1:128, 1:256）
        # Bit4: 边沿选择（0=上升沿，1=下降沿）
        # Bit5: 时钟源选择（0=内部，1=外部）
        # 注意：CONT寄存器的值直接对应分频系数，不需要额外计算
        cont_value = 0x00
        prescaler_val = config["prescaler"] & 0x07
        cont_value |= prescaler_val
        
        if config.get("edge", "rising") == "falling":
            cont_value |= 0x10
        
        if config["clock_source"] == "external":
            cont_value |= 0x20
        
        # 使用CONTW宏设置CONT寄存器
        # 分频比对应关系：0=1:2, 1=1:4, 2=1:8, 3=1:16, 4=1:32, 5=1:64, 6=1:128, 7=1:256
        prescaler_ratio = [2, 4, 8, 16, 32, 64, 128, 256][prescaler_val]
        self._add_code_with_comment(code, f"\tCONTW(0x{cont_value:02X});", f"TCC预分频\t;预分频比=1:{prescaler_ratio}")
        code.append("")
        
        # 中断使能配置（IOCF寄存器，在头文件中可能叫IMR）
        interrupt_config = self.config_data.get("interrupt", {})
        iocf_value = 0x00
        if interrupt_config.get("TCC", {}).get("enabled", False):
            iocf_value |= 0x01  # Bit0: TCIE = 1
        
        self._add_code_with_comment(code, f"\tIOCP_W(IMR, 0x{iocf_value:02X});", "TCC中断使能")
        code.append("")
        
        # TCC计数寄存器（R1，直接访问TCC）
        tcc_tim = config.get("count_value", 6)
        self._add_code_with_comment(code, f"\tTCC = TCC_TIM;\t\t\t//1/2 * 8 * (256-6) = 1000us\t公式：1/IRC频率 * 预分频 * （256-初值）", "")
        code.append("")
        
        # 清除中断标志位（清除TCIF，Bit0）
        self._add_code_with_comment(code, f"\tISR = 0xfe;", "清TCC中断标志位")
        
        # 注意：不在此处关闭函数，由调用方负责添加 "}" 结束符
        return code
    
    def _generate_tc0_init_code(self) -> List[str]:
        """生成TC0初始化代码"""
        code = []
        config = self.config_data["timer"]["TC0"]
        code.append("void file_tc0_Init(void)")
        code.append("{")
        self._add_comment(code, "===========TC0初始化==============")
        
        tc0con = 0x00
        prescaler_val = config["prescaler"] & 0x07
        tc0con |= prescaler_val
        
        if config["clock_source"] == "external":
            tc0con |= 0x10
            tc0con |= 0x20
        
        if config["clock_source"] == "system":
            tc0con |= 0x80
        
        self._add_code_with_comment(code, f"\tTC0CON = 0x{tc0con:02X};", "TC0控制寄存器")
        self._add_code_with_comment(code, f"\tTC0C = {config['count_value']};", "TC0计数寄存器")
        
        if config["interrupt"]:
            self._add_code_with_comment(code, f"\tINTE0 |= 0x01;", "中断使能")
        
        code.append("}")
        code.append("")
        return code
    
    def _generate_tc1_init_code(self) -> List[str]:
        """生成TC1初始化代码"""
        code = []
        config = self.config_data["timer"]["TC1"]
        code.append("void file_tc1_Init(void)")
        code.append("{")
        self._add_comment(code, "===========TC1初始化==============")
        comment = f"TC1配置: 模式={config['mode']}, 周期={config['period']}"
        self._add_comment(code, comment)
        code.append("}")
        code.append("")
        return code
    
    def _generate_tc2_init_code(self) -> List[str]:
        """生成TC2初始化代码"""
        code = []
        config = self.config_data["timer"]["TC2"]
        code.append("void file_tc2_Init(void)")
        code.append("{")
        self._add_comment(code, "===========TC2初始化==============")
        comment = f"TC2配置: 模式={config['mode']}, 周期={config['period']}"
        self._add_comment(code, comment)
        code.append("}")
        code.append("")
        return code
    
    def _generate_adc_init_code(self) -> List[str]:
        """生成ADC初始化代码"""
        code = []
        config = self.config_data["adc"]
        code.append("void file_adc_Init(void)")
        code.append("{")
        self._add_comment(code, "===========ADC初始化==============")
        
        # 计算P5ADE和P6ADE
        p5ade = 0x00
        p6ade = 0x00
        for ch in config["channels"]:
            if ch < 6:
                p5ade |= (1 << ch)
            else:
                p6ade |= (1 << (ch - 6))
        
        self._add_code_with_comment(code, f"\tP5ADE=0x{p5ade:02X};", "P5模拟端口控制")
        self._add_code_with_comment(code, f"\tP6ADE=0x{p6ade:02X};", "P6模拟端口控制")
        code.append("")
        
        # 参考电压和时钟分频
        vref_map = {"VDD": 0x00, "4V": 0x01, "3V": 0x02, "2V": 0x03, "1.5V": 0x04}
        clkdiv_map = {"Fosc/1": 0xC0, "Fosc/4": 0x40, "Fosc/16": 0x00, "Fosc/64": 0x80}
        
        adcon0 = vref_map.get(config["reference"], 0x00) | clkdiv_map.get(config["clock_div"], 0x00)
        self._add_code_with_comment(code, f"\tADCON0 = 0x{adcon0:02X};", "AD基准电压及分频选择")
        
        adcon1 = 0x40
        if config["calibration"]:
            adcon1 |= 0x10
        self._add_code_with_comment(code, f"\tADCON1 = 0x{adcon1:02X};", "AD使能")
        code.append("}")
        code.append("")
        return code
    
    def _generate_pwm_init_code(self) -> List[str]:
        """生成PWM初始化代码"""
        code = []
        code.append("void file_pwm_Init(void)")
        code.append("{")
        self._add_comment(code, "===========PWM初始化==============")
        # PWM初始化代码较复杂，这里简化处理
        # 完整实现需要根据芯片类型和配置生成
        code.append("}")
        code.append("")
        return code

