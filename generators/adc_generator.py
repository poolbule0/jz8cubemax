#!/usr/bin/env python
# -*- coding: gbk -*-
"""
ADC.C 代码生成器
生成ADC功能代码文件
"""

from .base_generator import BaseGenerator


class ADCGenerator(BaseGenerator):
    """ADC.C 代码生成器"""
    
    def generate(self) -> str:
        """生成ADC代码"""
        code = []
        code.append("#include \"main.h\"")
        code.append("#include \"ADC.H\"")
        code.append("")
        code.append("uint16_t ADC_value;")
        code.append("uint16_t ADC_GetValue(uint8_t chn, uint8_t vref)")
        code.append("{")
        code.append("\tuint16_t delay_time = 0;")
        code.append("\tuint16_t ADC_value_high = 0;")
        code.append("\tuint16_t ADC_value_low = 0xffff;")
        code.append("\tuint32_t ADC_value_sum = 0;")
        code.append("\tuint8_t count = 0;")
        code.append("")
        self._add_code_with_comment(code, "\tADIS = (chn << 4);", "AD采样口使能口")
        
        clkdiv_map = {"Fosc/1": "C_Ckl_Div1", "Fosc/4": "C_Ckl_Div4", 
                     "Fosc/16": "C_Ckl_Div16", "Fosc/64": "C_Ckl_Div64"}
        clkdiv = clkdiv_map.get(self.config_data["adc"]["clock_div"], "C_Ckl_Div16")
        self._add_code_with_comment(code, f"\tADCON0 = vref | {clkdiv};", "AD基准电压及分频选择")
        code.append("")
        self._add_code_with_comment(code, "\tADCON1 = C_ADC_START;", "AD使能，不校准")
        code.append("")
        code.append("\tfor(count = 0; count < 10; count++)")
        code.append("\t{")
        code.append("\t\tADRUN = 1;")
        code.append("\t\tdelay_time = DELAY_TIME;")
        code.append("\t\twhile(ADRUN && (--delay_time));")
        code.append("")
        code.append("\t\tADC_value = ADIS & 0x0f;")
        code.append("\t\tADC_value = (ADC_value << 8) + ADATL;")
        code.append("\t\tif(ADC_value > ADC_value_high)")
        code.append("\t\t{")
        code.append("\t\t\tADC_value_high = ADC_value;")
        code.append("\t\t}")
        code.append("\t\tif(ADC_value < ADC_value_low)")
        code.append("\t\t{")
        code.append("\t\t\tADC_value_low = ADC_value;")
        code.append("\t\t}")
        code.append("\t\tADC_value_sum += ADC_value;")
        code.append("\t}")
        code.append("")
        code.append("\tADC_value = (ADC_value_sum - ADC_value_high - ADC_value_low + 4) >> 3;")
        code.append("")
        code.append("\treturn ADC_value;")
        code.append("}")
        code.append("")
        
        return "\n".join(code)

