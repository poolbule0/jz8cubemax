#!/usr/bin/env python
# -*- coding: gbk -*-
"""
JZ8P1521 芯片实现
"""

from typing import Dict, Any, List
from .chip_base import ChipBase


class JZ8P1521(ChipBase):
    """
    JZ8P1521 芯片的具体实现。
    
    主要特性：
    - 1K × 14-Bit OTP ROM
    - 48 × 8-Bit SRAM
    - 12个I/O口（P5: 4个, P6: 8个）
    - 3路共周期8位PWM
    - 8位TCC定时器
    - LVD低压检测
    - WDT看门狗
    - 4个中断源
    """
    
    def get_chip_name(self) -> str:
        """返回芯片的名称"""
        return "JZ8P1521"
    
    def get_display_name(self) -> str:
        """返回芯片的显示名称"""
        return "JZ8P1521"
    
    def get_datasheet_path(self) -> str:
        """返回芯片数据手册的路径"""
        return "数据手册/JZ8P1521-V1.3.md"
    
    def get_example_path(self) -> str:
        """返回示例项目目录路径"""
        return "示例项目/1521"
    
    def get_header_file_name(self) -> str:
        """返回芯片主头文件的名称（用于包含，使用小写格式）"""
        return "jz8p1521.h"
    
    def get_default_config(self) -> Dict[str, Any]:
        """返回芯片的默认配置数据结构"""
        return {
            "gpio": {
                "P5": {
                    # P5只有4个引脚（P50-P53）
                    "direction": [0, 0, 0, 0],  # 0=输出, 1=输入
                    "pullup": [1, 1, 1, 1],      # 0=使能, 1=禁止
                    "pulldown": [1, 1, 1, 1]    # 0=使能, 1=禁止
                },
                "P6": {
                    # P6有8个引脚（P60-P67）
                    "direction": [0, 0, 0, 0, 0, 0, 0, 0],  # 默认输出
                    "pullup": [1, 1, 1, 1, 1, 1, 1, 1],      # 0=使能, 1=禁止
                    "pulldown": [1, 1, 1, 1, 1, 1, 1, 1],   # 0=使能, 1=禁止
                    "wakeup": [0, 0, 0, 0, 0, 0, 0, 0]      # 0=禁止, 1=使能
                }
            },
            "timer": {
                # JZ8P1521只有TCC定时器（8位）
                "TCC": {
                    "enabled": False,
                    "clock_source": "instruction",  # instruction, system, external
                    "prescaler": 0,      # 0-7对应不同分频（1:2到1:256）
                    "count_value": 0,   # TCC初始值
                    "edge": "rising",   # rising, falling（外部时钟时）
                    "interrupt": False
                }
            },
            "pwm": {
                # JZ8P1521只有3路PWM，共周期8位
                "PWM1": {
                    "enabled": False,
                    "period": 100,      # 周期值（0-255）
                    "duty": 50,         # 占空比（0-255）
                    "mapping": "P62",   # 映射到P62
                    "clock_source": "instruction",  # instruction, system
                    "prescaler": 0,     # T1分频比（0-8对应1:1到1:256）
                    "interrupt": False,
                    "invert": False     # PWM1互补输出
                },
                "PWM2": {
                    "enabled": False,
                    "period": 100,
                    "duty": 0,
                    "mapping": "P61",   # 映射到P61
                    "clock_source": "instruction",
                    "prescaler": 0,
                    "interrupt": False
                },
                "PWM3": {
                    "enabled": False,
                    "period": 100,
                    "duty": 0,
                    "mapping": "P60",   # 映射到P60
                    "clock_source": "instruction",
                    "prescaler": 0,
                    "interrupt": False
                }
            },
            "interrupt": {
                # JZ8P1521有4个中断源
                "TCC": {
                    "enabled": False,   # TCC溢出中断
                    "flag": "TCIF"
                },
                "EXINT": {
                    "enabled": False,   # 外部中断（P60/INT）
                    "flag": "EXIF"
                },
                "PORT_CHANGE": {
                    "enabled": False,   # P6端口状态改变中断
                    "flag": "ICIF"
                },
                "T1_PWM": {
                    "enabled": False,   # T1/PWM周期中断
                    "flag": "T1IF"
                }
            },
            "system": {
                "clock": {
                    "source": "IRC",     # IRC, HXT, LXT
                    "frequency": "8MHz", # 8MHz, 1MHz（IRC时）
                    "divider": 2        # 2, 4, 8, 16, 32 clock
                },
                "wdt": {
                    "enabled": False,
                    "timeout": "18ms"    # 4.5ms, 18ms, 72ms, 288ms
                },
                "lvr": {
                    "enabled": True,
                    "threshold": "2.4V"  # 1.2V-4.7V，0.1V/级
                },
                "lvd": {
                    "enabled": False,
                    "threshold": "2.4V", # 2.0V-4.7V，0.1V/级
                    "external": False    # 是否使用P63外部电压检测
                }
            },
            "sleep": {
                "enabled": False,
                "mode": "sleep",        # sleep（睡眠）, idle（空闲）
                "wakeup": {
                    "wdt": False,       # WDT唤醒
                    "port_change": False, # 端口变化唤醒
                    "tcc": False,       # TCC唤醒（空闲模式）
                    "pwm": False        # PWM唤醒（空闲模式）
                },
                "wake_ports": []       # 唤醒端口列表
            },
            "isr": {
                "enable_time_10ms": True,
                "time_10ms_threshold": 200,
                "time_10ms_flag": "Time_10ms",
                "enable_time_200us": False,  # 1521可能不需要200us定时
                "time_200us_threshold": 4,
                "time_200us_flag": "Time_200us",
                "reg_10ms_name": "reg_10ms",
                "reg_200us_name": "reg_200us"
            },
            "code_generation": {
                "include_comments": True
            }
        }
    
    def get_supported_modules(self) -> List[str]:
        """返回该芯片支持的配置模块列表"""
        # JZ8P1521不支持ADC，支持GPIO、TCC定时器、PWM、中断、睡眠、ISR
        return ["init", "main", "pwm", "sleep", "isr", "tcc"]
    
    def get_register_info(self) -> Dict[str, Any]:
        """返回芯片寄存器信息（用于代码生成）"""
        return {
            "page_system": True,  # 使用页面寄存器系统
            "registers": {
                # RPAGE寄存器
                "R1": "TCC",      # TCC定时计数器
                "R5": "PORT5",   # P5数据寄存器
                "R6": "PORT6",   # P6数据寄存器
                "R7": "LVDCON",  # LVD控制寄存器
                "R8": "PWMCON",  # PWM控制寄存器
                "R9": "PRD",     # PWM周期寄存器
                "RA": "PDC1",    # PWM1占空比
                "RB": "PDC2",    # PWM2占空比
                "RC": "PDC3",    # PWM3占空比
                "RD": "ICIECR",  # P6端口中断唤醒使能寄存器
                "RE": "CPUCON",  # CPU模式控制寄存器
                "RF": "RIFG",    # 中断标志寄存器
                # IOPAGE寄存器
                "IOC5": "P5CR",  # P5方向控制寄存器
                "IOC6": "P6CR",  # P6方向控制寄存器
                "IOC9": "PHDCR", # 端口上下拉控制寄存器
                "IOCB": "PDCR",  # 端口下拉控制寄存器
                "IOCD": "PHCR",  # P6端口上拉控制寄存器
                "IOCE": "WDTCR", # WDT控制寄存器
                "IOCF": "RIEN",  # 中断使能控制寄存器
                "CONT": "CONT"   # 控制寄存器
            }
        }

