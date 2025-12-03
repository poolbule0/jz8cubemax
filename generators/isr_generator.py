#!/usr/bin/env python
# -*- coding: gbk -*-
"""
isr.c 代码生成器
生成中断服务程序代码文件
"""

from .base_generator import BaseGenerator


class ISRGenerator(BaseGenerator):
    """isr.c 代码生成器"""
    
    def generate(self) -> str:
        """生成中断服务程序代码"""
        # 根据芯片类型选择不同的生成方法
        if self.chip_name == "JZ8P1521":
            return self._generate_1521()
        else:
            return self._generate_generic()
    
    def _generate_1521(self) -> str:
        """生成JZ8P1521的ISR代码"""
        cfg = self.config_data.get("isr", {})
        enable_time_10ms = cfg.get("enable_time_10ms", True)
        time_10ms_threshold = cfg.get("time_10ms_threshold", 1)
        time_10ms_flag = cfg.get("time_10ms_flag", "Time_10ms")
        enable_time_200us = cfg.get("enable_time_200us", False)
        time_200us_threshold = cfg.get("time_200us_threshold", 4)
        time_200us_flag = cfg.get("time_200us_flag", "Time_200us")
        reg_10ms_name = cfg.get("reg_10ms_name", "reg_10ms")
        reg_200us_name = cfg.get("reg_200us_name", "reg_200us")
        
        code = []
        code.append('#include"user.h"')
        code.append("")
        code.append(f"unsigned char {reg_200us_name};")
        code.append(f"unsigned char {reg_10ms_name};")
        code.append("volatile __at(0x10) uint8_t A_BUFF;\t\t//中断ACC保护RAM")
        code.append("volatile __at(0x11) uint8_t R3_BUFF;\t\t//中断STATUS保护RAM")
        code.append("")
        code.append("")
        code.append("void int_isr(void) __interrupt")
        code.append("{")
        self._add_code_with_comment(code, '\t__asm__("org 0x08");', "中断入口地址")
        code.append("\tDI();")
        self._add_code_with_comment(code, "\tPUSH(_A_BUFF,_R3_BUFF);", "中断入栈保护")
        
        # TCC中断处理
        self._add_comment(code, "=========Tcc中断程序===============//")
        code.append("\tif(TCIF == 1)\t\t\t\t//判断TCIF是否为1")
        code.append("\t{")
        
        # 重新加载TCC值（从配置中获取TCC_TIM）
        timer_config = self.config_data.get("timer", {}).get("TCC", {})
        tcc_tim = timer_config.get("count_value", 6)
        self._add_code_with_comment(code, f"\t\tTCC += TCC_TIM;\t\t\t//1/2 * 8 * (256-6) = 1000us\t公式：1/IRC频率 * 预分频 * （256-初值）", "")
        self._add_code_with_comment(code, f"\t\tISR = 0xfe;\t\t\t\t//清TC0中断标志位", "")
        code.append("")
        
        # 10ms定时处理
        if enable_time_10ms:
            code.append(f"\t\tif (++ {reg_10ms_name} >= {time_10ms_threshold})")
            code.append("\t\t{")
            code.append(f"\t\t\t{reg_10ms_name} = 0;")
            code.append(f"\t\t\t{time_10ms_flag} = ENABLE;")
            code.append("")
            code.append("\t\t}")
        
        # 200us定时处理（可选）
        if enable_time_200us:
            code.append("")
            code.append(f"\t\tif (++ {reg_200us_name} >= {time_200us_threshold})")
            code.append("\t\t{")
            code.append(f"\t\t\t{reg_200us_name} = 0;")
            code.append(f"\t\t\t{time_200us_flag} = ENABLE;")
            code.append("\t\t}")
        
        code.append("\t}")
        
        # 其他中断处理（EXINT, PORT_CHANGE, T1_PWM）
        interrupt_config = self.config_data.get("interrupt", {})
        has_other_interrupts = False
        
        if interrupt_config.get("EXINT", {}).get("enabled", False):
            has_other_interrupts = True
            self._add_comment(code, "=========外部中断程序===============//")
            code.append("\tif(EXIF == 1)\t\t\t\t//判断EXIF是否为1")
            code.append("\t{")
            self._add_code_with_comment(code, "\t\tISR = 0xfd;\t\t\t\t//清EXIF中断标志位", "")
            code.append("\t\t// 外部中断处理代码")
            code.append("\t}")
        
        if interrupt_config.get("PORT_CHANGE", {}).get("enabled", False):
            has_other_interrupts = True
            self._add_comment(code, "=========端口变化中断程序===============//")
            code.append("\tif(ICIF == 1)\t\t\t\t//判断ICIF是否为1")
            code.append("\t{")
            self._add_code_with_comment(code, "\t\tISR = 0xfb;\t\t\t\t//清ICIF中断标志位", "")
            code.append("\t\t// 端口变化中断处理代码")
            code.append("\t}")
        
        if interrupt_config.get("T1_PWM", {}).get("enabled", False):
            has_other_interrupts = True
            self._add_comment(code, "=========T1/PWM周期中断程序===============//")
            code.append("\tif(T1IF == 1)\t\t\t\t//判断T1IF是否为1")
            code.append("\t{")
            self._add_code_with_comment(code, "\t\tISR = 0xf7;\t\t\t\t//清T1IF中断标志位", "")
            code.append("\t\t// T1/PWM周期中断处理代码")
            code.append("\t}")
        
        # 清除不使用的中断标志位
        self._add_comment(code, "===============中断程序===============//")
        self._add_code_with_comment(code, "\tISR = 0x01;", "清不使用的中断标志位")
        
        # 恢复保护
        self._add_code_with_comment(code, "\tPOP(_A_BUFF,_R3_BUFF);", "中断出栈保护恢复")
        code.append("\tEI();")
        code.append("}")
        code.append("")
        
        return "\n".join(code)
    
    def _generate_generic(self) -> str:
        """生成通用芯片的ISR代码（保留原有逻辑）"""
        cfg = self.config_data.get("isr", {})
        enable_time_10ms = cfg.get("enable_time_10ms", True)
        time_10ms_threshold = cfg.get("time_10ms_threshold", 200)
        time_10ms_flag = cfg.get("time_10ms_flag", "Time_10ms")
        enable_time_200us = cfg.get("enable_time_200us", True)
        time_200us_threshold = cfg.get("time_200us_threshold", 4)
        time_200us_flag = cfg.get("time_200us_flag", "Time_200us")
        reg_10ms_name = cfg.get("reg_10ms_name", "reg_10ms")
        reg_200us_name = cfg.get("reg_200us_name", "reg_200us")
        
        code = []
        code.append('#include "main.h"')
        code.append('#include "type.h"')
        code.append("")
        code.append(f"unsigned char {reg_200us_name};")
        code.append(f"unsigned char {reg_10ms_name};")
        code.append("")
        code.append("volatile unsigned char __at(0x00) A_Buff;")
        code.append("volatile unsigned char __at(0x01) S_Buff;")
        code.append("")
        code.append("void int_isr(void) __interrupt")
        code.append("{")
        self._add_code_with_comment(code, '\t__asm__("org 0x08");', "中断入口地址")
        code.append("\tdi();")
        self._add_code_with_comment(code, "\tpush(A_Buff, S_Buff);", "中断入栈保护")
        self._add_comment(code, "=========TC0中断程序===============//")
        code.append("\tif(TC0IF == 1)")
        code.append("\t{")
        code.append("\t\tTC0C  += TCC_NUM;")
        code.append("\t\tTC0IF = 0;")
        code.append("")
        
        if enable_time_10ms:
            code.append(f"\t\tif(++{reg_10ms_name} >= {time_10ms_threshold})")
            code.append("\t\t{")
            code.append(f"\t\t\t{reg_10ms_name}  = 0;")
            code.append(f"\t\t\t{time_10ms_flag} = 1;")
            code.append("\t\t}")
            code.append("")
        
        if enable_time_200us:
            code.append(f"\t\tif(++{reg_200us_name} >= {time_200us_threshold})")
            code.append("\t\t{")
            code.append(f"\t\t\t{reg_200us_name}  = 0;")
            code.append(f"\t\t\t{time_200us_flag} = 1;")
            code.append("\t\t}")
            code.append("")
        
        code.append("\t}")
        self._add_code_with_comment(code, "\tINTF0=0x01;", "清除不用的标志位")
        code.append("\tINTF1=0x00;")
        self._add_code_with_comment(code, "\tpop(A_Buff, S_Buff);", "中断出栈保护恢复")
        code.append("\tei();")
        code.append("\tret();")
        code.append("}")
        code.append("")
        
        return "\n".join(code)

