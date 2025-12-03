#!/usr/bin/env python
# -*- coding: gbk -*-
"""
JZ8P2615 芯片实现
"""

from .chip_base import ChipBase
from typing import Dict, Any


class JZ8P2615Chip(ChipBase):
    """JZ8P2615 芯片实现类"""
    
    def get_chip_name(self) -> str:
        return "JZ8P2615"
    
    def get_display_name(self) -> str:
        return "JZ8P2615"
    
    def get_datasheet_path(self) -> str:
        return "JZ8P2615-V1.3.md"
    
    def get_example_path(self) -> str:
        return "示例项目"
    
    def get_header_file_name(self) -> str:
        return "JZ8P2615.h"
    
    def get_default_config(self) -> Dict[str, Any]:
        """返回 JZ8P2615 的默认配置"""
        return {
            "gpio": {
                "P5": {
                    "direction": [0, 0, 0, 0, 0, 0, 0, 0],  # 0=输出, 1=输入
                    "pullup": [1, 1, 1, 1, 1, 1, 1, 1],      # 0=使能, 1=禁止
                    "pulldown": [1, 1, 1, 1, 1, 1, 1, 1],    # 0=使能, 1=禁止
                    "wakeup": [0, 0, 0, 0, 0, 0, 0, 0]       # 0=禁止, 1=使能
                },
                "P6": {
                    "direction": [0, 0, 0, 0, 0, 0, 0, 0],
                    "pullup": [1, 1, 1, 1, 1, 1, 1, 1],
                    "pulldown": [1, 1, 1, 1, 1, 1, 1, 1],
                    "opendrain": [0, 0, 0, 0, 0, 0, 0, 0],   # 0=禁止, 1=使能
                    "weakdrive": [0, 0, 0, 0, 0, 0, 0, 0],   # 0=禁止, 1=使能
                    "wakeup": [0, 0, 0, 0, 0, 0, 0, 0]
                }
            },
            "adc": {
                "enabled": False,
                "channels": [],
                "reference": "VDD",
                "clock_div": "Fosc/16",
                "calibration": False
            },
            "timer": {
                "TC0": {
                    "enabled": False,
                    "clock_source": "system",
                    "prescaler": 0,
                    "count_value": 206,
                    "interrupt": False
                },
                "TC1": {
                    "enabled": False,
                    "mode": "10bit",
                    "prescaler": 0,
                    "period": 1000,
                    "pwm_enabled": False,
                    "interrupt": False
                },
                "TC2": {
                    "enabled": False,
                    "mode": "10bit",
                    "prescaler": 0,
                    "period": 1000,
                    "pwm_enabled": False,
                    "interrupt": False
                }
            },
            "pwm": {
                "PWM1": {"enabled": False, "period": 100, "duty": 50, "mapping": "P60", "clock_source": "instruction"},
                "PWM2": {"enabled": False, "period": 100, "duty": 0, "mapping": "P61", "clock_source": "instruction"},
                "PWM3": {"enabled": False, "period": 100, "duty": 40, "mapping": "P62", "clock_source": "instruction"},
                "PWM4": {"enabled": False, "period": 23,  "duty": 0,  "mapping": "P63", "clock_source": "instruction"}
            },
            "interrupt": {
                "wdtcon": {
                    "wdt_enabled": False,
                    "int0_enabled": False,
                    "int1_enabled": False,
                    "vfoe": False,
                    "int1_edge": "falling",
                    "int0_edge": "falling"
                },
                "inte0": {
                    "ad_ie": False,
                    "ex1_ie": False,
                    "ex0_ie": False,
                    "p6ic_ie": False,
                    "p5ic_ie": False,
                    "tc0_ie": False
                },
                "inte1": {
                    "dt4_ie": False,
                    "dt3_ie": False,
                    "dt2_ie": False,
                    "dt1_ie": False,
                    "tc2_ie": False,
                    "tc1_ie": False
                },
                "INT0": {"enabled": False, "edge": "rising"},
                "INT1": {"enabled": False, "edge": "rising"},
                "port_change": {
                    "P5": False,
                    "P6": False
                }
            },
            "system": {
                "clock": {
                    "source": "IHRC",
                    "frequency": "8MHz",
                    "divider": 1
                },
                "wdt": {
                    "enabled": False,
                    "timeout": 0
                },
                "lvr": {
                    "enabled": True,
                    "threshold": "2.4V"
                }
            },
            "isr": {
                "enable_time_10ms": True,
                "time_10ms_threshold": 200,
                "time_10ms_flag": "Time_10ms",
                "enable_time_200us": True,
                "time_200us_threshold": 4,
                "time_200us_flag": "Time_200us",
                "reg_10ms_name": "reg_10ms",
                "reg_200us_name": "reg_200us"
            },
            "sleep": {
                "enabled": False,
                "counter_name": "sleep_cnt",
                "threshold": 5,
                "condition": "F_CHARGE == 0 && F_CHARGE_FULL == 0 && r_g_workMod == 0",
                "wake_ports": ["P6"]
            },
            "code_generation": {
                "include_comments": True
            }
        }

