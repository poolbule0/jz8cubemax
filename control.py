#!/usr/bin/env python
# -*- coding: gbk -*-
"""
JZ8P2615 代码生成工具 - 控制逻辑模块
负责配置管理、数据手册解析、代码生成等核心功能
"""

import os
import json
import re
from typing import Dict, List, Optional, Any, Tuple


class ConfigController:
    """配置控制器 - 管理所有配置数据和代码生成逻辑"""
    
    def __init__(self):
        """初始化控制器"""
        self.config_data = self._init_default_config()
        self.datasheet_path = "JZ8P2615-V1.3.md"
        self.example_path = "示例项目"
        self.register_map = {}
        self.code_templates = {}
        
        # 加载数据手册和示例代码
        self._load_datasheet()
        self._load_example_code()
        self.type_header_template = self._load_type_header()
    
    def _init_default_config(self) -> Dict[str, Any]:
        """初始化默认配置"""
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
                "channels": [],  # 使用的通道列表
                "reference": "VDD",     # 参考电压: VDD, 4V, 3V, 2V, 1.5V
                "clock_div": "Fosc/16", # 时钟分频: Fosc/1, Fosc/4, Fosc/16, Fosc/64
                "calibration": False    # 是否校准
            },
            "timer": {
                "TC0": {
                    "enabled": False,
                    "clock_source": "system",  # system, instruction, external
                    "prescaler": 0,      # 0-7对应不同分频
                    "count_value": 206,
                    "interrupt": False
                },
                "TC1": {
                    "enabled": False,
                    "mode": "10bit",  # 10bit, 20bit
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
                # 每个PWM通道：是否使能、周期、占空比、引脚映射
                # 映射选项依据数据手册 R1C6/PWMIS:
                # PWM1S: 0=P60, 1=P52
                # PWM2S: 0=P61, 1=P53
                # PWM3S: 0=P62, 1=P54
                # PWM4S: 0=P63, 1=P55
                "PWM1": {"enabled": False, "period": 100, "duty": 50, "mapping": "P60", "clock_source": "instruction"},
                "PWM2": {"enabled": False, "period": 100, "duty": 0, "mapping": "P61", "clock_source": "instruction"},
                "PWM3": {"enabled": False, "period": 100, "duty": 40, "mapping": "P62", "clock_source": "instruction"},
                "PWM4": {"enabled": False, "period": 23,  "duty": 0,  "mapping": "P63", "clock_source": "instruction"}
            },
            "interrupt": {
                # WDTCON寄存器配置
                "wdtcon": {
                    "wdt_enabled": False,      # Bit7: WDT使能
                    "int0_enabled": False,     # Bit6: P60外部中断使能
                    "int1_enabled": False,     # Bit5: P53外部中断使能
                    "vfoe": False,             # Bit4: 内部基准输出使能
                    "int1_edge": "falling",    # Bit3: INT1触发沿 (rising/falling)
                    "int0_edge": "falling"     # Bit2: INT0触发沿 (rising/falling)
                },
                # INTE0寄存器配置
                "inte0": {
                    "ad_ie": False,            # Bit5: ADC中断使能
                    "ex1_ie": False,           # Bit4: INT1中断使能
                    "ex0_ie": False,           # Bit3: INT0中断使能
                    "p6ic_ie": False,          # Bit2: P6端口变化中断使能
                    "p5ic_ie": False,          # Bit1: P5端口变化中断使能
                    "tc0_ie": False            # Bit0: TC0中断使能
                },
                # INTE1寄存器配置
                "inte1": {
                    "dt4_ie": False,           # Bit5: DT4中断使能
                    "dt3_ie": False,            # Bit4: DT3中断使能
                    "dt2_ie": False,            # Bit3: DT2中断使能
                    "dt1_ie": False,            # Bit2: DT1中断使能
                    "tc2_ie": False,            # Bit1: TC2中断使能
                    "tc1_ie": False             # Bit0: TC1中断使能
                },
                # 兼容旧配置（外部中断、端口变化）
                "INT0": {"enabled": False, "edge": "rising"},  # rising, falling
                "INT1": {"enabled": False, "edge": "rising"},
                "port_change": {
                    "P5": False,
                    "P6": False
                }
            },
            "system": {
                "clock": {
                    "source": "IHRC",
                    "frequency": "8MHz",  # 8MHz, 6MHz, 5.4MHz, 4.8MHz, 3.4MHz, 1MHz
                    "divider": 1
                },
                "wdt": {
                    "enabled": False,
                    "timeout": 0
                },
                "lvr": {
                    "enabled": True,
                    "threshold": "2.4V"  # 2.4V, 1.8V, 1.6V, 1.2V
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
            }
        }
    
    def _load_datasheet(self):
        """加载数据手册，提取寄存器信息"""
        if not os.path.exists(self.datasheet_path):
            print(f"警告: 数据手册文件不存在: {self.datasheet_path}")
            return
        
        try:
            content = self._read_file_with_encoding(self.datasheet_path)
            
            # 提取寄存器地址定义（从JZ8P2615.h中获取更准确）
            self._parse_register_map()
            
            print(f"数据手册加载成功: {self.datasheet_path}")
        except Exception as e:
            print(f"加载数据手册失败: {e}")
    
    def _parse_register_map(self):
        """解析寄存器映射表"""
        # 从JZ8P2615.h文件中提取寄存器地址
        header_file = os.path.join(self.example_path, "JZ8P2615.h")
        if not os.path.exists(header_file):
            print(f"警告: 头文件不存在: {header_file}")
            return
        
        try:
            content = self._read_file_with_encoding(header_file)
            
            # 使用正则表达式提取寄存器地址定义
            # 格式: #define REG_NAME_ADDR 0xXXX
            pattern = r'#define\s+(\w+_ADDR)\s+0X([0-9A-F]+)'
            matches = re.findall(pattern, content, re.IGNORECASE)
            
            for reg_name, addr in matches:
                # 去掉_ADDR后缀，获取寄存器名
                reg_base_name = reg_name.replace('_ADDR', '')
                self.register_map[reg_base_name] = {
                    'address': int(addr, 16),
                    'name': reg_base_name
                }
            
            print(f"寄存器映射表加载成功，共 {len(self.register_map)} 个寄存器")
        except Exception as e:
            print(f"解析寄存器映射表失败: {e}")
    
    def _load_example_code(self):
        """加载示例代码，提取代码模板"""
        if not os.path.exists(self.example_path):
            print(f"警告: 示例代码目录不存在: {self.example_path}")
            return
        
        try:
            # 加载初始化代码模板
            init_file = os.path.join(self.example_path, "init.c")
            if os.path.exists(init_file):
                self.code_templates['init'] = self._read_file_with_encoding(init_file)
            
            # 加载主程序模板
            main_file = os.path.join(self.example_path, "main.c")
            if os.path.exists(main_file):
                self.code_templates['main'] = self._read_file_with_encoding(main_file)
            
            # 加载ADC代码模板
            adc_file = os.path.join(self.example_path, "ADC.C")
            if os.path.exists(adc_file):
                self.code_templates['adc'] = self._read_file_with_encoding(adc_file)
            
            print(f"示例代码模板加载成功，共 {len(self.code_templates)} 个模板")
        except Exception as e:
            print(f"加载示例代码失败: {e}")
    
    def _load_type_header(self) -> str:
        """加载type.h模板"""
        type_path = os.path.join(self.example_path, "type.h")
        if not os.path.exists(type_path):
            return ""
        try:
            return self._read_file_with_encoding(type_path)
        except Exception as e:
            print(f"加载type.h失败: {e}")
            return ""
    
    def _read_file_with_encoding(self, filepath: str) -> str:
        """以GBK优先的方式读取文件"""
        try:
            with open(filepath, 'r', encoding='gbk') as f:
                return f.read()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
    
    def get_config(self) -> Dict[str, Any]:
        """获取当前配置"""
        return self.config_data
    
    def update_config(self, module: str, config: Dict[str, Any]):
        """更新配置"""
        if module in self.config_data:
            self.config_data[module].update(config)
        else:
            self.config_data[module] = config
    
    def save_config(self, filepath: str):
        """保存配置到文件"""
        try:
            # JSON文件使用UTF-8编码更通用
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.config_data, f, indent=4, ensure_ascii=False)
            print(f"配置已保存到: {filepath}")
            return True
        except Exception as e:
            print(f"保存配置失败: {e}")
            return False
    
    def load_config(self, filepath: str):
        """从文件加载配置"""
        try:
            # JSON文件使用UTF-8编码更通用
            with open(filepath, 'r', encoding='utf-8') as f:
                self.config_data = json.load(f)
            print(f"配置已从文件加载: {filepath}")
            return True
        except Exception as e:
            print(f"加载配置失败: {e}")
            return False
    
    def get_register_map(self) -> Dict[str, Any]:
        """获取寄存器映射表"""
        return self.register_map
    
    def get_code_templates(self) -> Dict[str, str]:
        """获取代码模板"""
        return self.code_templates
    
    def generate_init_code(self) -> str:
        """生成初始化代码"""
        code = []
        code.append("#include \"init.h\"")
        code.append("#include \"type.h\"")
        code.append("#include \"main.h\"")
        code.append("#include \"JZ8P2615.h\"")
        code.append("")
        code.append("void file_clrRam(void)")
        code.append("{")
        code.append("\tfor(RSR=0x90;RSR<0xFF;RSR++)\t//清零 BANK0 RAM  IAR-R0,RSR-R4")
        code.append("\t{IAR = 0;}")
        code.append("\t IAR = 0;")
        code.append("}")
        code.append("//===================================//")
        code.append("//端口初始化")
        code.append("//===================================//")
        code.append("void file_init(void)")
        code.append("{")
        code.append("//===========端口初始化=============")
        
        # 生成GPIO配置代码
        gpio_config = self.config_data["gpio"]
        
        # 计算寄存器值
        p5con = self._calculate_port_control(gpio_config["P5"]["direction"])
        p6con = self._calculate_port_control(gpio_config["P6"]["direction"])
        p5ph = self._calculate_port_pull(gpio_config["P5"]["pullup"])
        p6ph = self._calculate_port_pull(gpio_config["P6"]["pullup"])
        p5pd = self._calculate_port_pull(gpio_config["P5"]["pulldown"])
        p6pd = self._calculate_port_pull(gpio_config["P6"]["pulldown"])
        p6od = self._calculate_port_pull(gpio_config["P6"]["opendrain"], invert=True)
        p6wd = self._calculate_port_pull(gpio_config["P6"]["weakdrive"], invert=True)
        p5iwe = self._calculate_port_pull(gpio_config["P5"]["wakeup"], invert=True)
        p6iwe = self._calculate_port_pull(gpio_config["P6"]["wakeup"], invert=True)
        
        code.append(f"\tPORT5=0x00;")
        code.append(f"\tPORT6=0x00;")
        code.append("")
        code.append(f"\tP5CON=0x{p5con:02X};\t\t//P5端口控制\t;0输出，1输入")
        code.append(f"\tP6CON=0x{p6con:02X};\t\t//P6端口控制    ;0输出，1输入")
        code.append("")
        code.append(f"\tP5PH=0x{p5ph:02X};\t\t//P5口上拉\t\t;0使能，1禁止")
        code.append(f"\tP6PH=0x{p6ph:02X};\t\t//P6口上拉\t\t;0使能，1禁止")
        code.append("")
        code.append(f"\tP5PD=0x{p5pd:02X};\t\t//P5口下拉\t\t;0使能，1禁止")
        code.append(f"\tP6PD=0x{p6pd:02X};\t\t//P6口下拉\t\t;0使能，1禁止")
        code.append("")
        code.append(f"\tP6OD=0x{p6od:02X};\t\t//P6口开漏\t\t;0禁止，1使能")
        code.append(f"\tP6WD=0x{p6wd:02X};\t\t//P6口弱驱动   ;0禁止，1使能")
        code.append("")
        code.append("\t//-----端口变化中断唤醒------")
        code.append(f"\tP5IWE=0x{p5iwe:02X};\t\t//P5口状态变化唤醒使能")
        code.append(f"\tP6IWE=0x{p6iwe:02X};\t\t//P6口状态变化唤醒使能")
        code.append("")
        
        # 中断配置
        wdtcon = self._compute_wdtcon_value()
        inte0 = self._compute_inte0_value()
        inte1 = self._compute_inte1_value()
        
        code.append("\t// -----使能外部中断设置------")
        code.append(f"\tWDTCON=0x{wdtcon:02X};\t\t//bit6&5:P60&P53外部中断功能控制位，0:普通IO口, 1:外部中断口")
        code.append("")
        code.append(f"\tINTE0=0x{inte0:02X};\t\t//中断使能")
        code.append(f"\tINTE1=0x{inte1:02X};\t\t//周期及占空比中断")
        code.append(f"\tINTF0=0x00;\t\t//清中断标志位")
        code.append(f"\tINTF1=0x00;")
        code.append("}")
        code.append("")
        
        # 生成定时器初始化代码
        if self.config_data["timer"]["TC0"]["enabled"]:
            code.extend(self._generate_tc0_init_code())
        
        if self.config_data["timer"]["TC1"]["enabled"]:
            code.extend(self._generate_tc1_init_code())
        
        if self.config_data["timer"]["TC2"]["enabled"]:
            code.extend(self._generate_tc2_init_code())
        
        # 生成ADC初始化代码
        if self.config_data["adc"]["enabled"]:
            code.extend(self._generate_adc_init_code())
        
        # 生成PWM初始化代码
        pwm_enabled = any(self.config_data["pwm"][pwm]["enabled"] for pwm in ["PWM1", "PWM2", "PWM3", "PWM4"])
        if pwm_enabled:
            code.extend(self._generate_pwm_init_code())
        
        return "\n".join(code)
    
    def _calculate_port_control(self, direction_list):
        """计算端口控制寄存器值"""
        value = 0
        for i, dir_val in enumerate(direction_list):
            if dir_val == 1:  # 输入
                value |= (1 << i)
        return value
    
    def _calculate_port_pull(self, pull_list, invert=False):
        """计算上拉/下拉寄存器值"""
        value = 0
        for i, pull_val in enumerate(pull_list):
            if invert:
                # 对于开漏、弱驱动、唤醒：0=禁止，1=使能
                if pull_val == 1:  # 使能
                    value |= (1 << i)
            else:
                # 对于上拉/下拉：0=使能，1=禁止
                # 寄存器位：0=使能，1=禁止
                # 所以如果配置是1（禁止），寄存器位应该是1
                if pull_val == 1:  # 禁止，寄存器位设为1
                    value |= (1 << i)
                # 如果配置是0（使能），寄存器位应该是0，不需要设置
        return value
    
    def _generate_tc0_init_code(self):
        """生成TC0初始化代码"""
        code = []
        config = self.config_data["timer"]["TC0"]
        code.append("void file_tc0_Init(void)")
        code.append("{")
        code.append("\t//===========TC0初始化==============")
        
        # TC0CON寄存器计算
        tc0con = 0x00
        # 分频器设置 (bit 0-2: TCOPSR<2:0>)
        # 映射关系: 0=1:2, 1=1:4, 2=1:8, 3=1:16, 4=1:32, 5=1:64, 6=1:128, 7=1:256
        prescaler_val = config["prescaler"] & 0x07
        prescaler_map = {0: "1:2", 1: "1:4", 2: "1:8", 3: "1:16", 
                         4: "1:32", 5: "1:64", 6: "1:128", 7: "1:256"}
        tc0con |= prescaler_val
        # PAB位 (bit 3): 0=分给TC0, 1=分给WDT
        # 这里默认分给TC0
        # TE位 (bit 4): 边沿选择
        if config["clock_source"] == "external":
            tc0con |= 0x10  # TE=1
        # TS位 (bit 5): 信号源选择
        if config["clock_source"] == "external":
            tc0con |= 0x20  # TS=1
        # TCOCKS位 (bit 7): 时钟选择
        if config["clock_source"] == "system":
            tc0con |= 0x80  # TCOCKS=1
        
        code.append(f"\tTC0CON = 0x{tc0con:02X};\t//TC0控制寄存器 (TCOPSR={prescaler_val}, 分频={prescaler_map[prescaler_val]})")
        code.append(f"\tTC0C = {config['count_value']};\t\t//TC0计数寄存器")
        
        if config["interrupt"]:
            code.append(f"\tINTE0 |= 0x01;\t\t//中断使能")
        
        code.append("}")
        code.append("")
        return code
    
    def _generate_tc1_init_code(self):
        """生成TC1初始化代码"""
        code = []
        config = self.config_data["timer"]["TC1"]
        code.append("void file_tc1_Init(void)")
        code.append("{")
        code.append("\t//===========TC1初始化==============")
        code.append(f"\t// TC1配置: 模式={config['mode']}, 周期={config['period']}")
        code.append("}")
        code.append("")
        return code
    
    def _generate_tc2_init_code(self):
        """生成TC2初始化代码"""
        code = []
        config = self.config_data["timer"]["TC2"]
        code.append("void file_tc2_Init(void)")
        code.append("{")
        code.append("\t//===========TC2初始化==============")
        code.append(f"\t// TC2配置: 模式={config['mode']}, 周期={config['period']}")
        code.append("}")
        code.append("")
        return code
    
    def _generate_adc_init_code(self):
        """生成ADC初始化代码"""
        code = []
        config = self.config_data["adc"]
        code.append("void file_adc_Init(void)")
        code.append("{")
        code.append("\t//===========ADC初始化==============")
        
        # 计算P5ADE和P6ADE
        p5ade = 0x00
        p6ade = 0x00
        for ch in config["channels"]:
            if ch < 6:
                p5ade |= (1 << ch)
            else:
                p6ade |= (1 << (ch - 6))
        
        code.append(f"\tP5ADE=0x{p5ade:02X};\t\t//P5模拟端口控制")
        code.append(f"\tP6ADE=0x{p6ade:02X};\t\t//P6模拟端口控制")
        code.append("")
        
        # 参考电压和时钟分频
        vref_map = {"VDD": 0x00, "4V": 0x01, "3V": 0x02, "2V": 0x03, "1.5V": 0x04}
        clkdiv_map = {"Fosc/1": 0xC0, "Fosc/4": 0x40, "Fosc/16": 0x00, "Fosc/64": 0x80}
        
        adcon0 = vref_map.get(config["reference"], 0x00) | clkdiv_map.get(config["clock_div"], 0x00)
        code.append(f"\tADCON0 = 0x{adcon0:02X};\t//AD基准电压及分频选择")
        
        adcon1 = 0x40  # ADEN=1
        if config["calibration"]:
            adcon1 |= 0x10  # CALI=1
        code.append(f"\tADCON1 = 0x{adcon1:02X};\t//AD使能")
        code.append("}")
        code.append("")
        return code
    
    def _generate_pwm_init_code(self):
        """生成PWM初始化代码"""
        code = []
        code.append("void file_pwm_Init(void)")
        code.append("{")
        code.append("\t//===========PWM初始化==============")
        pwm_config = self.config_data["pwm"]
        for pwm_name in ["PWM1", "PWM2", "PWM3", "PWM4"]:
            if pwm_config[pwm_name]["enabled"]:
                code.append(f"\t// {pwm_name}配置: 周期={pwm_config[pwm_name]['period']}, 占空比={pwm_config[pwm_name]['duty']}")
        code.append("}")
        code.append("")
        return code
    
    def generate_main_code(self) -> str:
        """生成主程序代码"""
        code = []
        cfg_isr = self.config_data.get("isr", {})
        t10_flag = cfg_isr.get("time_10ms_flag", "Time_10ms")
        t200_flag = cfg_isr.get("time_200us_flag", "Time_200us")
        
        code.append("#include \"JZ8P2615.h\"")
        code.append("#include \"main.h\"")
        code.append("#include \"init.h\"")
        code.append("#include \"type.h\"")
        if self.config_data.get("sleep", {}).get("enabled"):
            code.append("#include \"sleep.h\"")
        code.append("")
        # 定义在 main.h 中声明的全局变量
        code.append("SYS_FlgBitClass U_Flage1;")
        code.append("uint8_t r_g_workMod = 0;")
        code.append("")
        
        # 根据配置添加头文件
        if self.config_data["adc"]["enabled"]:
            code.append("#include \"ADC.H\"")
        code.append("")
        code.append("void main(void)")
        code.append("{")
        code.append("\tfile_clrRam();")
        code.append("\tfile_init();\t\t\t\t//初始化")
        
        # 根据配置添加初始化调用
        if self.config_data["timer"]["TC0"]["enabled"]:
            code.append("\tfile_tc0_Init();")
        if self.config_data["timer"]["TC1"]["enabled"]:
            code.append("\tfile_tc1_Init();")
        if self.config_data["timer"]["TC2"]["enabled"]:
            code.append("\tfile_tc2_Init();")
        if self.config_data["adc"]["enabled"]:
            code.append("\tfile_adc_Init();")
        if any(self.config_data["pwm"][pwm]["enabled"] for pwm in ["PWM1", "PWM2", "PWM3", "PWM4"]):
            code.append("\tfile_pwm_Init();")
        
        code.append("\tei();")
        code.append("")
        code.append("\twhile(1)")
        code.append("\t{")
        code.append("\t\t// 用户代码区域")
        code.append("")
        code.append(f"\t\tif ({t200_flag})")
        code.append("\t\t{")
        code.append(f"\t\t\t{t200_flag} = 0;")
        code.append("\t\t\t// 在这里处理 200us 周期任务")
        code.append("\t\t}")
        code.append("")
        code.append(f"\t\tif ({t10_flag})")
        code.append("\t\t{")
        code.append(f"\t\t\t{t10_flag} = 0;")
        code.append("\t\t\t// 在这里处理 10ms 周期任务")
        if self.config_data.get("sleep", {}).get("enabled"):
            code.append("\t\t\tsleep_scan();")
        code.append("\t\t}")
        code.append("\t}")
        code.append("}")
        code.append("")
        
        return "\n".join(code)
    
    def generate_all_files(self) -> Dict[str, str]:
        """生成所有文件（C文件和H文件）"""
        files = {}
        
        # 生成init.c和init.h
        files["init.c"] = self.generate_init_code()
        files["init.h"] = self.generate_init_header()
        
        # 生成isr.c
        files["isr.c"] = self.generate_isr_code()

        # 睡眠代码
        if self.config_data.get("sleep", {}).get("enabled"):
            files["sleep.c"] = self.generate_sleep_code()
            files["sleep.h"] = self.generate_sleep_header()

        # 生成main.c和main.h（基础模板）
        files["main.c"] = self.generate_main_code()
        files["main.h"] = self.generate_main_header()
        
        # 如果启用 ADC，则把示例项目中封装好的 ADC.C / ADC.H 原样拷贝出来
        if self.config_data.get("adc", {}).get("enabled"):
            adc_c_path = os.path.join(self.example_path, "ADC.C")
            adc_h_path = os.path.join(self.example_path, "ADC.H")
            if os.path.exists(adc_c_path):
                files["ADC.C"] = self._read_file_with_encoding(adc_c_path)
            if os.path.exists(adc_h_path):
                files["ADC.H"] = self._read_file_with_encoding(adc_h_path)
        
        # 如果任意 PWM 使能，生成 pwm.c / pwm.h（可配置周期和占空比）
        pwm_cfg = self.config_data.get("pwm", {})
        pwm_enabled = any(
            pwm_cfg.get(ch, {}).get("enabled")
            for ch in ["PWM1", "PWM2", "PWM3", "PWM4"]
        )
        if pwm_enabled:
            files["pwm.c"] = self.generate_pwm_code()
            files["pwm.h"] = self.generate_pwm_header()
        
        # type.h 模板
        files["type.h"] = self.generate_type_header()
        
        return files

    def generate_pwm_header(self) -> str:
        """生成 pwm.h 头文件（基于示例，加入可配置开关）"""
        cfg_pwm = self.config_data.get("pwm", {})
        
        code: List[str] = []
        code.append("#ifndef __PWM_H__")
        code.append("#define __PWM_H__")
        code.append("")
        code.append("#include \"type.h\"")
        code.append("#include \"main.h\"")
        code.append("")
        channel_order = [("PWM1", "fw_pwm1Init"), ("PWM2", "fw_pwm2Init"),
                         ("PWM3", "fw_pwm3Init"), ("PWM4", "fw_pwm4Init")]
        for ch_key, func_name in channel_order:
            if cfg_pwm.get(ch_key, {}).get("enabled"):
                code.append(f"void {func_name}(void);")
        code.append("")
        code.append("#endif")
        code.append("")
        return "\n".join(code)

    def generate_pwm_code(self) -> str:
        """生成 pwm.c 源文件，允许配置周期和占空比"""
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
            if clock == "system":
                return "\tPWMCON |= 0x40;\t\t//PWM时钟 = 系统周期"
            return "\tPWMCON |= 0x00;\t\t//PWM时钟 = 指令周期"

        code: List[str] = []
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

            code.append(f"//==========={section_title}初始化============")
            code.append(f"\t{tc_con_line}")

            if ch_name in ("PWM1", "PWM2"):
                code.append(f"\tTC1PRDTH = 0x{tc_prdth:02X};\t//TC1周期高2位 / PWM1占空比高2位" if ch_name == "PWM1"
                            else f"\tTC2PRDTH = 0x{tc_prdth:02X};\t//TC2周期高2位 / PWM2占空比高2位")
                code.append(f"\tTC1PRDL = 0x{prd_low:02X};\t\t//TC1（PWM1、PWM3）周期低8位" if ch_name == "PWM1"
                            else f"\tTC2PRDL = 0x{prd_low:02X};\t\t//TC2（PWM2/PWM4）周期低8位")
                code.append(f"\tPWM1DTL = 0x{duty_low:02X};\t\t//PWM1占空比低8位" if ch_name == "PWM1"
                            else f"\tPWM2DTL = 0x{duty_low:02X};\t\t//PWM2占空比低位寄存器")
            elif ch_name == "PWM3":
                code.append(f"\tTC1PRDTH = 0x{tc_prdth:02X};\t//TC1（PWM1、PWM3）周期高2位")
                code.append(f"\tTC1PRDL = 0x{prd_low:02X};\t\t//TC1（PWM1、PWM3）周期低8位")
                code.append("")
                code.append(f"\tPWM3DTH = 0x{duty_high:02X};\t\t//PWM3占空比高位寄存器")
                code.append(f"\tPWM3DTL = 0x{duty_low:02X};\t\t//PWM3占空比低位寄存器")
            else:  # PWM4
                code.append("")
                code.append(f"\tTC2PRDTH = 0x{tc_prdth:02X};\t//TC2周期高2位")
                code.append(f"\tTC2PRDL = 0x{prd_low:02X};\t\t//TC2（PWM2/PWM4）周期低8位")
                code.append("")
                code.append(f"\tPWM4DTH = 0x{duty_high:02X};\t\t//PWM4占空比高位寄存器")
                code.append(f"\tPWM4DTL = 0x{duty_low:02X};\t\t//PWM4占空比低位寄存器")

            map_pin = pwm_cfg.get("mapping", "P60" if ch_name == "PWM1" else
                                  "P61" if ch_name == "PWM2" else
                                  "P62" if ch_name == "PWM3" else "P63")

            if ch_name == "PWM1":
                code.append("")
                if map_pin == "P52":
                    code.append("\tPWMIS |= 0x01;\t\t\t//PWM1 映射到 P52")
                else:
                    code.append("\tPWMIS &= ~0x01;\t\t\t//PWM1 映射到 P60")
            elif ch_name == "PWM2":
                code.append("")
                if map_pin == "P53":
                    code.append("\tPWMIS |= 0x04;\t\t\t//PWM2 映射到 P53")
                else:
                    code.append("\tPWMIS &= ~0x04;\t\t\t//PWM2 映射到 P61")
            elif ch_name == "PWM3":
                code.append("")
                if map_pin == "P54":
                    code.append("\tPWMIS |= 0x10;\t\t\t//PWM3 映射到 P54")
                else:
                    code.append("\tPWMIS &= ~0x10;\t\t\t//PWM3 映射到 P62")
            else:
                code.append("")
                if map_pin == "P55":
                    code.append("\tPWMIS |= 0x40;\t\t\t//PWM4 映射到 P55")
                else:
                    code.append("\tPWMIS &= ~0x40;\t\t\t//PWM4 映射到 P63")
                code.append("")
                code.append("\tDEADCON |= 0x20;\t\t//死区控制寄存器（示例默认开启 PWM2/4 死区）")

            code.append("}")

        if first_function:
            code.append("// 当前未启用任何 PWM 通道")
        code.append("")
        return "\n".join(code)
    
    def generate_main_header(self) -> str:
        """生成main.h头文件"""
        code = []
        code.append("")
        code.append("#ifndef __MAIN_H__")
        code.append("#define __MAIN_H__")
        code.append("")
        code.append("#include \"JZ8P2615.h\"")
        code.append("#include \"type.h\"")
        code.append("")
        
        # 根据配置添加TC0计数常量
        if self.config_data["timer"]["TC0"]["enabled"]:
            count_val = self.config_data["timer"]["TC0"]["count_value"]
            code.append(f"#define\tTCC_NUM\t{count_val}")
            code.append("")
        
        # 添加GPIO定义（根据配置）
        gpio_defs = []
        gpio_config = self.config_data["gpio"]
        
        # 检查P5端口配置，生成定义
        for pin in range(8):
            if gpio_config["P5"]["direction"][pin] == 0:  # 输出
                gpio_defs.append(f"#define\tIo_P5{pin}\t\tPORT5_{pin}")
        
        # 检查P6端口配置，生成定义
        for pin in range(8):
            if gpio_config["P6"]["direction"][pin] == 0:  # 输出
                gpio_defs.append(f"#define\tIo_P6{pin}\t\tPORT6_{pin}")
        
        if gpio_defs:
            code.extend(gpio_defs)
            code.append("")
        
        # 添加标志位结构体定义
        code.append("typedef struct SYS_FlgBit_")
        code.append("{")
        code.append("\tuint8_t bit0:1;")
        code.append("\tuint8_t bit1:1;")
        code.append("\tuint8_t bit2:1;")
        code.append("\tuint8_t bit3:1;")
        code.append("\tuint8_t bit4:1;")
        code.append("\tuint8_t bit5:1;")
        code.append("\tuint8_t bit6:1;")
        code.append("\tuint8_t bit7:1;")
        code.append("}SYS_FlgBit;")
        code.append("typedef union SYS_FlgBitClass_")
        code.append("{")
        code.append("\tuint8_t\t\tFlgAll;")
        code.append("\tSYS_FlgBit\tSYS_Flg;")
        code.append("}SYS_FlgBitClass;")
        code.append("")
        cfg_isr = self.config_data.get("isr", {})
        t10_flag = cfg_isr.get("time_10ms_flag", "Time_10ms")
        t200_flag = cfg_isr.get("time_200us_flag", "Time_200us")
        code.append("extern SYS_FlgBitClass\tU_Flage1;")
        code.append(f"#define\t{t10_flag}\t\t\t(U_Flage1.SYS_Flg.bit0)")
        code.append(f"#define {t200_flag}\t\t\t(U_Flage1.SYS_Flg.bit1)")
        code.append("#define\tF_WORK_START\t\t\t(U_Flage1.SYS_Flg.bit2)")
        code.append("#define\tF_CHARGE_H_IO\t\t\t(U_Flage1.SYS_Flg.bit3)")
        code.append("#define\tF_CHARGE\t\t\t\t(U_Flage1.SYS_Flg.bit4)")
        code.append("#define\tF_CHARGE_FULL\t\t\t(U_Flage1.SYS_Flg.bit5)")
        code.append("#define\tF_FIRST_POWER_UP\t\t(U_Flage1.SYS_Flg.bit6)")
        code.append("")
        code.append("/**************** 定义寄存器 ******************/")
        code.append("")
        code.append("extern uint8_t r_g_workMod;")
        code.append("")
        code.append("")
        code.append("#endif")
        code.append("")
        
        return "\n".join(code)
    
    def generate_isr_code(self) -> str:
        """生成isr.c代码"""
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
        code.append('\t__asm__("org 0x08");\t\t//中断入口地址')
        code.append("\tdi();")
        code.append("\tpush(A_Buff, S_Buff);\t\t//中断入栈保护")
        code.append("\t//=========TC0中断程序===============//")
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
        code.append("\tINTF0=0x01;\t\t\t//清除不用的标志位")
        code.append("\tINTF1=0x00;")
        code.append("\tpop(A_Buff, S_Buff);\t\t//中断出栈保护恢复")
        code.append("\tei();")
        code.append("\tret();")
        code.append("}")
        code.append("")
        
        return "\n".join(code)
    
    def generate_sleep_code(self) -> str:
        """生成sleep.c代码"""
        cfg = self.config_data.get("sleep", {})
        counter = cfg.get("counter_name", "sleep_cnt")
        threshold = cfg.get("threshold", 5)
        # 原始条件字符串（可能为空）
        raw_condition = cfg.get(
            "condition",
            "F_CHARGE == 0 && F_CHARGE_FULL == 0 && r_g_workMod == 0",
        )
        condition = (raw_condition or "").strip()
        
        code = []
        code.append('#include "sleep.h"')
        code.append('#include "type.h"')
        code.append('#include "main.h"')
        code.append('#include "init.h"')
        code.append(f"unsigned char {counter} = 0;")
        code.append("//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        code.append("//***************睡眠程序*****************")
        code.append("//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        code.append("void sleep_scan(void)")
        code.append("{")
        # 如果条件不为空，生成外层 if (condition) { ... } else { ... }
        if condition:
            code.append(f"\tif({condition})")
            code.append("\t{")
            indent = "\t\t"
        else:
            # 条件为空时，不需要外部 if 语句，直接执行计数与睡眠逻辑
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
        code.append(f"{indent}\tINTE0=0x{wake_bits:02X};\t// 睡眠唤醒端口配置")
        code.append("")
        code.append(f"{indent}\tINTF0 = 0;")
        code.append(f"{indent}\tINTF1 = 0;")
        code.append(f"{indent}\tdi();\t\t\t//禁止唤醒进入中断")
        code.append(f"{indent}\tsleep();")
        code.append(f"{indent}\tnop();")
        code.append(f"{indent}\tnop();")
        code.append(f"{indent}\tnop();")
        code.append(f"{indent}\tnop();")
        code.append(f"{indent}\tcwdt();")
        code.append(f"{indent}\t//------------睡眠唤醒----------------------")
        inte0_value = self._compute_inte0_value()
        inte1_value = self._compute_inte1_value()
        code.append(f"{indent}\tINTE0 = 0x{inte0_value:02X};")
        code.append(f"{indent}\tINTE1 = 0x{inte1_value:02X};")
        if self.config_data["timer"]["TC0"]["enabled"]:
            code.append(f"{indent}\tfile_tc0_Init();")
        code.append("")
        code.append(f"{indent}\tINTF0 = 0;")
        code.append(f"{indent}\tINTF1 = 0;")
        code.append(f"{indent}\tei();")
        code.append(f"{indent}" + "}")

        # 条件不为空时，再补齐 else 分支（重置计数器）
        if condition:
            code.append("\t}")
            code.append("\telse")
            code.append("\t{")
            code.append(f"\t\t{counter} = 0;")
            code.append("\t}")
        code.append("}")
        code.append("")
        
        return "\n".join(code)
    
    def generate_sleep_header(self) -> str:
        code = []
        code.append("#ifndef __SLEEP_H__")
        code.append("#define __SLEEP_H__")
        code.append("")
        code.append("void sleep_scan(void);")
        code.append("")
        code.append("#endif")
        code.append("")
        return "\n".join(code)
    
    def generate_type_header(self) -> str:
        """生成type.h文件"""
        if self.type_header_template:
            return self.type_header_template
        return (
            "#ifndef _TYPE_H_\n"
            "#define _TYPE_H_\n"
            "\n"
            "#include \"JZ8P2615.h\"\n"
            "\n"
            "#define ei()  __asm__(\" ei \")\n"
            "#define di()  __asm__(\" di \")\n"
            "#define nop() __asm__(\" nop \")\n"
            "#define sleep() __asm__(\" sleep \")\n"
            "#define cwdt() __asm__(\" cwdt \")\n"
            "#define ret() __asm__(\" ret \")\n"
            "\n"
            "#define ctw(val)\t        __asm__(\"mov a,@\"#val\"\\n ctw\")\n"
            "#define iw(reg,val)\t\t    __asm__(\"mov a,@\"#val\"\\n iw \"#reg)\n"
            "#define ir(ram,reg)\t\t    __asm__(\"ir \"#reg\"\\n mov \"#ram\",a\")\n"
            "#define push(a_reg,R3_reg)\t__asm__(\"mov _\"#a_reg\",a\\n swap _\"#a_reg\"\\n swapa STATUS\\n mov _\"#R3_reg\",a\")\n"
            "#define pop(a_reg,R3_reg)\t__asm__(\"swapa _\"#R3_reg\"\\n mov STATUS,a\\n swapa _\"#a_reg)\")\n"
            "#define rcr2(h1,l1)\t     __asm__(\"btc _STATUSbits,0\\n rcr _\"#h1\"\\n rcr _\"#l1)\")\n"
            "\n"
            "typedef   unsigned char        uint8_t;\n"
            "typedef   unsigned int         uint16_t;\n"
            "typedef   unsigned long        uint32_t;\n"
            "\n"
            "#define   ENABLE    1\n"
            "#define   DISABLE   0\n"
            "\n"
            "#endif /* _TYPE_H_ */\n"
        )
    
    def _compute_wdtcon_value(self) -> int:
        int_config = self.config_data["interrupt"]
        wdtcon = 0x00
        wdtcon_config = int_config["wdtcon"]
        if wdtcon_config["wdt_enabled"]:
            wdtcon |= 0x80  # Bit7: WDT使能
        if wdtcon_config["int0_enabled"]:
            wdtcon |= 0x40  # Bit6: P60外部中断使能
        if wdtcon_config["int1_enabled"]:
            wdtcon |= 0x20  # Bit5: P53外部中断使能
        if wdtcon_config["vfoe"]:
            wdtcon |= 0x10  # Bit4: 内部基准输出使能
        if wdtcon_config["int1_edge"] == "rising":
            wdtcon |= 0x08  # Bit3: INT1上升沿触发
        if wdtcon_config["int0_edge"] == "rising":
            wdtcon |= 0x04  # Bit2: INT0上升沿触发
        return wdtcon
    
    def _compute_inte0_value(self) -> int:
        int_config = self.config_data["interrupt"]
        inte0 = 0x00
        inte0_config = int_config["inte0"]
        if inte0_config["ad_ie"]:
            inte0 |= 0x20
        if inte0_config["ex1_ie"]:
            inte0 |= 0x10
        if inte0_config["ex0_ie"]:
            inte0 |= 0x08
        if inte0_config["p6ic_ie"]:
            inte0 |= 0x04
        if inte0_config["p5ic_ie"]:
            inte0 |= 0x02
        if inte0_config["tc0_ie"]:
            inte0 |= 0x01
        return inte0
    
    def _compute_inte1_value(self) -> int:
        int_config = self.config_data["interrupt"]
        inte1 = 0x00
        inte1_config = int_config["inte1"]
        if inte1_config["dt4_ie"]:
            inte1 |= 0x20
        if inte1_config["dt3_ie"]:
            inte1 |= 0x10
        if inte1_config["dt2_ie"]:
            inte1 |= 0x08
        if inte1_config["dt1_ie"]:
            inte1 |= 0x04
        if inte1_config["tc2_ie"]:
            inte1 |= 0x02
        if inte1_config["tc1_ie"]:
            inte1 |= 0x01
        return inte1
    
    def generate_init_header(self) -> str:
        """生成init.h头文件"""
        code = []
        code.append("#ifndef __INIT_H__")
        code.append("#define __INIT_H__")
        code.append("")
        code.append("void file_clrRam(void);")
        code.append("void file_init(void);")
        code.append("")
        
        # 根据配置添加初始化函数声明
        if self.config_data["timer"]["TC0"]["enabled"]:
            code.append("void file_tc0_Init(void);")
        if self.config_data["timer"]["TC1"]["enabled"]:
            code.append("void file_tc1_Init(void);")
        if self.config_data["timer"]["TC2"]["enabled"]:
            code.append("void file_tc2_Init(void);")
        if self.config_data["adc"]["enabled"]:
            code.append("void file_adc_Init(void);")
        if any(self.config_data["pwm"][p]["enabled"] for p in ["PWM1", "PWM2", "PWM3", "PWM4"]):
            code.append("void file_pwm_Init(void);")
        
        code.append("")
        code.append("#endif")
        code.append("")
        
        return "\n".join(code)
    
    def generate_adc_code(self) -> str:
        """生成ADC.C文件"""
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
        code.append("\tADIS = (chn << 4);\t\t\t//AD采样口使能口")
        
        # 根据配置生成时钟分频
        clkdiv_map = {"Fosc/1": "C_Ckl_Div1", "Fosc/4": "C_Ckl_Div4", 
                     "Fosc/16": "C_Ckl_Div16", "Fosc/64": "C_Ckl_Div64"}
        clkdiv = clkdiv_map.get(self.config_data["adc"]["clock_div"], "C_Ckl_Div16")
        code.append(f"\tADCON0 = vref | {clkdiv};\t//AD基准电压及分频选择")
        code.append("")
        code.append("\tADCON1 = C_ADC_START;\t//AD使能，不校准")
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
    
    def generate_adc_header(self) -> str:
        """生成ADC.H头文件"""
        code = []
        code.append("#ifndef _FW_ADC_H_")
        code.append("#define _FW_ADC_H_")
        code.append("")
        code.append("#include \"type.h\"")
        code.append("")
        code.append("// ADC数据定义")
        code.append("enum")
        code.append("{")
        code.append("\tE_AD0_P50 = 0,")
        code.append("\tE_AD1_P51,")
        code.append("\tE_AD2_P52,")
        code.append("\tE_AD3_P53,")
        code.append("\tE_AD4_P54,")
        code.append("\tE_AD5_P55,")
        code.append("\tE_AD6_P60,")
        code.append("\tE_AD7_P61,")
        code.append("\tE_AD8_P62,")
        code.append("\tE_AD9_P63,")
        code.append("\tE_AD10_P64,")
        code.append("\tE_AD11_P65,")
        code.append("\tE_AD12_P66,")
        code.append("\tE_AD13_P67,")
        code.append("\tE_AD14,")
        code.append("};")
        code.append("enum")
        code.append("{")
        code.append("\tE_Vrefh_VDD = 0,\t\t// ADC reference high voltage is VDD")
        code.append("\tE_Vrefh_4V,\t\t\t// ADC reference high voltage is 4V")
        code.append("\tE_Vrefh_3V,\t\t\t// ADC reference high voltage is 3V")
        code.append("\tE_Vrefh_2V,\t\t\t// ADC reference high voltage is 2V")
        code.append("\tE_Vrefh_1_5V,\t\t\t// ADC reference high voltage is 1.5V")
        code.append("};")
        code.append("#define\tC_Ckl_Div16\t\t0x00\t\t// ADC clock is Fosc/16")
        code.append("#define\tC_Ckl_Div4\t\t0x40\t\t// ADC clock is Fosc/4")
        code.append("#define\tC_Ckl_Div64\t\t0x80\t\t// ADC clock is Fosc/64")
        code.append("#define\tC_Ckl_Div1\t\t0xC0\t\t// ADC clock is Fosc/1")
        code.append("")
        code.append("#define\tC_ADC_START\t\t0x40\t\t// ADC Start")
        code.append("")
        code.append("#define\tDELAY_TIME\t\t3000")
        code.append("")
        code.append("uint16_t\tADC_GetValue(uint8_t chn, uint8_t vref);")
        code.append("")
        code.append("#endif")
        code.append("")
        
        return "\n".join(code)
    
    def validate_config(self) -> Tuple[bool, List[str]]:
        """验证配置的有效性"""
        errors = []
        
        # TODO: 实现配置验证逻辑
        # 检查配置冲突、约束条件等
        
        return len(errors) == 0, errors

