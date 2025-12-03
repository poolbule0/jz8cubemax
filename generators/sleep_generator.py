#!/usr/bin/env python
# -*- coding: gbk -*-
"""
sleep.c 代码生成器
生成睡眠功能代码文件
"""

from .base_generator import BaseGenerator
from utils.register_calc import compute_inte0_value, compute_inte1_value


class SleepGenerator(BaseGenerator):
    """sleep.c 代码生成器"""
    
    def generate(self) -> str:
        """生成睡眠功能代码"""
        # 根据芯片类型选择不同的生成方法
        if self.chip_name == "JZ8P1521":
            return self._generate_1521()
        else:
            return self._generate_generic()
    
    def _generate_1521(self) -> str:
        """生成JZ8P1521的睡眠代码"""
        cfg = self.config_data.get("sleep", {})
        counter = cfg.get("counter_name", "sleep_cnt")
        threshold = cfg.get("threshold", 10)
        raw_condition = cfg.get("condition", "F_CHARGE == 0")
        condition = (raw_condition or "").strip()
        
        code = []
        code.append('#include "sleep.h"')
        code.append(f"unsigned char {counter} = 0;")
        code.append("void fw_sleepEvent()")
        code.append("{")
        
        if condition:
            code.append(f"\tif({condition})")
            code.append("\t{")
            indent = "\t\t"
        else:
            indent = "\t"

        code.append(f"{indent}if(++{counter} > {threshold})")
        code.append(f"{indent}" + "{")
        code.append(f"{indent}\t{counter} = 0;")
        code.append("")
        
        # 睡眠前准备
        # 关闭LVD
        self._add_code_with_comment(code, f"{indent}\tLVDCON = 0;", "关LVD")
        code.append("")
        
        # 关闭所有中断
        self._add_code_with_comment(code, f"{indent}\tIOCP_W(IMR, 0x00);", "关闭中断")
        
        # 关闭看门狗
        self._add_code_with_comment(code, f"{indent}\tIOCP_W(WDTCR, 0x00);", "关闭看门狗")
        
        # 清中断标志位
        self._add_code_with_comment(code, f"{indent}\tISR = 0;", "清中断标志位")
        
        # 禁止中断
        self._add_code_with_comment(code, f"{indent}\tDI();", "禁止唤醒进入中断")
        
        # 配置唤醒源（端口变化中断）
        wakeup_config = cfg.get("wakeup", {})
        iocf_value = 0x00
        if wakeup_config.get("port_change", False):
            iocf_value |= 0x02  # Bit1: ICIE = 1 (端口变化中断使能)
        if wakeup_config.get("tcc", False):
            iocf_value |= 0x01  # Bit0: TCIE = 1 (TCC中断使能)
        if wakeup_config.get("wdt", False):
            # WDT唤醒通过IOCE寄存器配置
            pass
        
        # 端口变化唤醒：根据 GPIO 的 P6.wakeup 位 和 sleep.wake_ports 来决定
        wake_ports = cfg.get("wake_ports", [])
        p6_selected = ("P6" in wake_ports)
        
        # 从 GPIO 配置计算 RD(ICIECR) 位图（Bit0~7 => P60~P67，1=使能）
        rd_value = 0x00
        gpio_p6_wakeup = self.config_data.get("gpio", {}).get("P6", {}).get("wakeup", [0]*8)
        try:
            for pin in range(8):
                if pin < len(gpio_p6_wakeup) and gpio_p6_wakeup[pin] == 1:
                    rd_value |= (1 << pin)
        except Exception:
            pass
        
        # 是否需要打开端口变化唤醒：勾选了 P6唤醒 或 显式开启 port_change 或 GPIO 中有任意 P6 位启用
        need_port_change = p6_selected or wakeup_config.get("port_change", False) or (rd_value != 0)
        
        # 若有端口唤醒需求，先写 RD，再打开 IMR.ICIE
        if need_port_change:
            if rd_value != 0:
                self._add_code_with_comment(code, f"{indent}\tRD = 0x{rd_value:02X};", "P6端口状态变化唤醒使能（ICIECR）;0禁止，1使能")
            iocf_value |= 0x02
        
        # 配置唤醒相关中断（IMR寄存器）
        # 注意：必须先设置RD寄存器，再设置IMR中的ICIE位才能使端口变化中断唤醒生效
        self._add_code_with_comment(code, f"{indent}\tIOCP_W(IMR, 0x{iocf_value:02X});", "配置唤醒相关中断（ICIE/TCIE 等）")
        code.append("")
        
        # 进入睡眠
        code.append(f"{indent}\tSLEEP();")
        code.append(f"{indent}\tNOP();")
        code.append(f"{indent}\tNOP();")
        code.append(f"{indent}\tNOP();")
        code.append(f"{indent}\tNOP();")
        code.append(f"{indent}\tCWDT();")
        code.append("")
        
        # 睡眠唤醒后恢复
        self._add_comment(code, "------------睡眠唤醒----------------------")
        
        # 重新初始化TCC定时器（如果使能）
        # 注意：必须在恢复中断前重新初始化定时器
        timer_config = self.config_data.get("timer", {})
        if timer_config.get("TCC", {}).get("enabled", False):
            code.append(f"{indent}\tfw_tc0Init();")
        
        # 清中断标志位（清除唤醒时产生的中断标志）
        self._add_code_with_comment(code, f"{indent}\tISR = 0x00;", "清中断标志位")
        code.append("")
        
        # 恢复中断使能
        interrupt_config = self.config_data.get("interrupt", {})
        iocf_restore = 0x00
        if interrupt_config.get("TCC", {}).get("enabled", False):
            iocf_restore |= 0x01  # TCIE
        if interrupt_config.get("EXINT", {}).get("enabled", False):
            iocf_restore |= 0x04  # EXIE
        if interrupt_config.get("PORT_CHANGE", {}).get("enabled", False):
            iocf_restore |= 0x02  # ICIE
        if interrupt_config.get("T1_PWM", {}).get("enabled", False):
            iocf_restore |= 0x08  # T1IE
        
        if iocf_restore != 0:
            self._add_code_with_comment(code, f"{indent}\tIOCP_W(IMR, 0x{iocf_restore:02X});", "恢复中断使能")
        
        # 使能中断
        code.append(f"{indent}\tEI();")
        
        code.append(f"{indent}" + "}")

        if condition:
            code.append("\t}")
        code.append("")
        code.append("}")
        code.append("")
        
        return "\n".join(code)
    
    def _generate_generic(self) -> str:
        """生成通用芯片的睡眠代码（保留原有逻辑）"""
        cfg = self.config_data.get("sleep", {})
        counter = cfg.get("counter_name", "sleep_cnt")
        threshold = cfg.get("threshold", 5)
        raw_condition = cfg.get("condition", "F_CHARGE == 0 && F_CHARGE_FULL == 0 && r_g_workMod == 0")
        condition = (raw_condition or "").strip()
        
        code = []
        code.append('#include "sleep.h"')
        code.append('#include "type.h"')
        code.append('#include "main.h"')
        code.append('#include "init.h"')
        code.append(f"unsigned char {counter} = 0;")
        self._add_comment(code, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        self._add_comment(code, "***************睡眠程序*****************")
        self._add_comment(code, "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        code.append("void sleep_scan(void)")
        code.append("{")
        
        if condition:
            code.append(f"\tif({condition})")
            code.append("\t{")
            indent = "\t\t"
        else:
            indent = "\t"

        code.append(f"{indent}if(++ {counter} >= {threshold})")
        code.append(f"{indent}" + "{")
        code.append(f"{indent}\t{counter} = 0;")
        code.append("")
        code.append(f"{indent}\tADIS = 0;")
        code.append(f"{indent}\tADCON0 = 0;")
        code.append(f"{indent}\tADCON1 = 0;")
        code.append(f"{indent}\tPORT5 = 0x00;")
        code.append(f"{indent}\tPORT6 = 0x00;")
        code.append("")
        code.append(f"{indent}\tTC0C = 0;")
        code.append(f"{indent}\tWDTCON = 0x00;")
        wake_bits = 0x00
        wake_ports = cfg.get("wake_ports", ["P6"])
        if "P5" in wake_ports:
            wake_bits |= 0x02
        if "P6" in wake_ports:
            wake_bits |= 0x04
        self._add_code_with_comment(code, f"{indent}\tINTE0=0x{wake_bits:02X};", "睡眠唤醒端口配置")
        code.append("")
        code.append(f"{indent}\tINTF0 = 0;")
        code.append(f"{indent}\tINTF1 = 0;")
        self._add_code_with_comment(code, f"{indent}\tdi();", "禁止唤醒进入中断")
        code.append(f"{indent}\tsleep();")
        code.append(f"{indent}\tnop();")
        code.append(f"{indent}\tnop();")
        code.append(f"{indent}\tnop();")
        code.append(f"{indent}\tnop();")
        code.append(f"{indent}\tcwdt();")
        self._add_comment(code, "------------睡眠唤醒----------------------")
        inte0_value = compute_inte0_value(self.config_data["interrupt"])
        inte1_value = compute_inte1_value(self.config_data["interrupt"])
        code.append(f"{indent}\tINTE0 = 0x{inte0_value:02X};")
        code.append(f"{indent}\tINTE1 = 0x{inte1_value:02X};")
        if self.config_data["timer"]["TC0"]["enabled"]:
            code.append(f"{indent}\tfile_tc0_Init();")
        code.append("")
        code.append(f"{indent}\tINTF0 = 0;")
        code.append(f"{indent}\tINTF1 = 0;")
        code.append(f"{indent}\tei();")
        code.append(f"{indent}" + "}")

        if condition:
            code.append("\t}")
            code.append("\telse")
            code.append("\t{")
            code.append(f"\t\t{counter} = 0;")
            code.append("\t}")
        code.append("}")
        code.append("")
        
        return "\n".join(code)

