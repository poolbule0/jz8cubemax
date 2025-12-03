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

# 导入芯片支持模块
try:
    from chips import ChipRegistry, ChipBase
    CHIPS_AVAILABLE = True
except ImportError:
    CHIPS_AVAILABLE = False
    print("警告: 芯片支持模块未找到，使用默认 JZ8P2615 配置")

# 导入新的工具模块
from utils.file_utils import read_file_with_encoding
from utils.register_calc import (
    calculate_port_control,
    calculate_port_pull,
    compute_wdtcon_value,
    compute_inte0_value,
    compute_inte1_value
)

# 导入代码生成器模块
from generators import (
    InitGenerator,
    MainGenerator,
    ISRGenerator,
    SleepGenerator,
    ADCGenerator,
    PWMGenerator
)


class ConfigController:
    """配置控制器 - 管理所有配置数据和代码生成逻辑"""
    
    def __init__(self, chip_name: Optional[str] = None):
        """
        初始化控制器
        
        Args:
            chip_name: 芯片名称，如果为None则使用默认芯片
        """
        # 初始化芯片
        if CHIPS_AVAILABLE:
            self.chip_registry = ChipRegistry()
            if chip_name:
                self.current_chip = self.chip_registry.get_chip(chip_name)
                if not self.current_chip:
                    print(f"警告: 芯片 {chip_name} 未找到，使用默认芯片")
                    self.current_chip = self.chip_registry.get_default_chip()
            else:
                self.current_chip = self.chip_registry.get_default_chip()
            
            if not self.current_chip:
                raise ValueError("没有可用的芯片实现")
            
            # 从芯片对象获取配置
            self.config_data = self.current_chip.get_default_config()
            self.datasheet_path = self.current_chip.datasheet_path
            self.example_path = self.current_chip.example_path
            self.register_map = self.current_chip.get_register_map()
            self.chip_name = self.current_chip.get_chip_name()
            self.header_file_name = self.current_chip.get_header_file_name()
        else:
            # 兼容旧版本：如果没有芯片模块，使用硬编码的 JZ8P2615 配置
            self.chip_registry = None
            self.current_chip = None
            self.config_data = self._init_default_config()
            self.datasheet_path = "JZ8P2615-V1.3.md"
            self.example_path = "示例项目"
            self.register_map = {}
            self.chip_name = "JZ8P2615"
            self.header_file_name = "JZ8P2615.h"
        
        self.code_templates = {}
        
        # 加载数据手册和示例代码
        self._load_datasheet()
        self._load_example_code()
        self.type_header_template = self._load_type_header()
        
        # 初始化代码生成器
        self._init_generators()
    
    def _is_chip_1521(self) -> bool:
        """判断当前芯片是否为 JZ8P1521"""
        return self.chip_name == "JZ8P1521"
    
    def _get_register_name(self, reg_type: str) -> str:
        """
        根据芯片类型获取寄存器名称
        
        Args:
            reg_type: 寄存器类型，如 "P5CON", "P6CON", "P5PH", "P6PH" 等
            
        Returns:
            对应芯片的寄存器名称
        """
        if self._is_chip_1521():
            # JZ8P1521 使用 IOC5/IOC6 等寄存器，需要页面切换
            reg_map_1521 = {
                "P5CON": "IOC5",  # P5方向控制寄存器
                "P6CON": "IOC6",  # P6方向控制寄存器
                "P5PH": "IOC9",   # P5上拉控制（IOC9的低4位）
                "P6PH": "IOCD",   # P6上拉控制寄存器
                "P5PD": "IOCB",   # P5下拉控制（IOCB的低4位）
                "P6PD": "IOC9",   # P6下拉控制（IOC9的高4位和IOCB的6:4位）
                "P6OD": None,     # JZ8P1521 不支持开漏
                "P6WD": None,     # JZ8P1521 不支持弱驱动
                "P5IWE": None,    # JZ8P1521 P5不支持唤醒
                "P6IWE": "RD"     # P6端口中断唤醒使能寄存器（RPAGE-RD）
            }
            return reg_map_1521.get(reg_type, reg_type)
        else:
            # JZ8P2615 使用标准寄存器名称
            return reg_type
    
    def switch_chip(self, chip_name: str) -> bool:
        """
        切换芯片
        
        Args:
            chip_name: 目标芯片名称
            
        Returns:
            是否切换成功
        """
        if not CHIPS_AVAILABLE or not self.chip_registry:
            print("错误: 芯片支持模块不可用")
            return False
        
        new_chip = self.chip_registry.get_chip(chip_name)
        if not new_chip:
            print(f"错误: 芯片 {chip_name} 未找到")
            return False
        
        # 切换芯片
        self.current_chip = new_chip
        self.config_data = new_chip.get_default_config()
        self.datasheet_path = new_chip.datasheet_path
        self.example_path = new_chip.example_path
        self.register_map = new_chip.get_register_map()
        self.chip_name = new_chip.get_chip_name()
        self.header_file_name = new_chip.get_header_file_name()
        
        # 重新加载数据手册和示例代码
        self._load_datasheet()
        self._load_example_code()
        self.type_header_template = self._load_type_header()
        
        print(f"已切换到芯片: {new_chip.get_display_name()}")
        return True
    
    def get_available_chips(self) -> Dict[str, str]:
        """
        获取所有可用的芯片列表
        
        Returns:
            芯片名称到显示名称的映射字典
        """
        if CHIPS_AVAILABLE and self.chip_registry:
            return self.chip_registry.get_chip_display_names()
        return {"JZ8P2615": "JZ8P2615"}
    
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
            },
            "code_generation": {
                "include_comments": True  # 是否在生成的代码中包含注释
            }
        }
    
    def _load_datasheet(self):
        """加载数据手册，提取寄存器信息"""
        if not os.path.exists(self.datasheet_path):
            print(f"警告: 数据手册文件不存在: {self.datasheet_path}")
            return
        
        try:
            content = read_file_with_encoding(self.datasheet_path)
            
            # 提取寄存器地址定义（从JZ8P2615.h中获取更准确）
            self._parse_register_map()
            
            print(f"数据手册加载成功: {self.datasheet_path}")
        except Exception as e:
            print(f"加载数据手册失败: {e}")
    
    def _parse_register_map(self):
        """解析寄存器映射表（兼容旧版本，如果使用芯片模块则不需要）"""
        # 如果使用芯片模块，寄存器映射已经从芯片对象获取，不需要重新解析
        if self.current_chip and self.register_map:
            return
        
        # 兼容旧版本：从头文件中提取寄存器地址
        header_file = os.path.join(self.example_path, self.header_file_name)
        if not os.path.exists(header_file):
            print(f"警告: 头文件不存在: {header_file}")
            return
        
        try:
            content = read_file_with_encoding(header_file)
            
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
                self.code_templates['init'] = read_file_with_encoding(init_file)
            
            # 加载主程序模板
            main_file = os.path.join(self.example_path, "main.c")
            if os.path.exists(main_file):
                self.code_templates['main'] = read_file_with_encoding(main_file)
            
            # 加载ADC代码模板
            adc_file = os.path.join(self.example_path, "ADC.C")
            if os.path.exists(adc_file):
                self.code_templates['adc'] = read_file_with_encoding(adc_file)
            
            print(f"示例代码模板加载成功，共 {len(self.code_templates)} 个模板")
        except Exception as e:
            print(f"加载示例代码失败: {e}")
    
    def _load_type_header(self) -> str:
        """加载type.h模板"""
        type_path = os.path.join(self.example_path, "type.h")
        if not os.path.exists(type_path):
            return ""
        try:
            return read_file_with_encoding(type_path)
        except Exception as e:
            print(f"加载type.h失败: {e}")
            return ""
    
    def _init_generators(self):
        """初始化代码生成器"""
        # 代码生成器将在需要时动态创建，这里只做准备工作
        pass
    
    def _read_file_with_encoding(self, filepath: str) -> str:
        """以GBK优先的方式读取文件（使用utils模块）"""
        return read_file_with_encoding(filepath)
    
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
    
    def _should_include_comments(self) -> bool:
        """检查是否应该包含注释"""
        return self.config_data.get("code_generation", {}).get("include_comments", True)
    
    def _add_comment(self, code_list: List[str], comment: str, inline: bool = False) -> None:
        """
        根据配置决定是否添加注释
        
        Args:
            code_list: 代码列表
            comment: 注释内容（不包含 // 或 /* */）
            inline: 是否为行内注释（True）或独立注释行（False）
        """
        if not self._should_include_comments():
            return
        
        # 如果注释本身就是代码行（例如分隔符），并且禁用了注释，则不应添加
        if comment.strip().startswith("//") or comment.strip().startswith("/*"):
            code_list.append(comment)
        else:
            code_list.append(f"// {comment}")

    def _add_code_with_comment(self, code_list: List[str], code_line: str, comment: str = "") -> None:
        """
        添加代码行，可选择性地添加行内注释
        
        Args:
            code_list: 代码列表
            code_line: 代码行（不包含注释）
            comment: 可选的注释内容
        """
        # 移除代码行中可能存在的注释
        clean_line = code_line.split("//")[0].rstrip()

        if not clean_line:
            # 如果移除注释后行为空，则不添加任何内容
            return

        if comment and self._should_include_comments():
            code_list.append(f"{clean_line}\t\t// {comment}")
        else:
            code_list.append(clean_line)
    
    def generate_init_code(self) -> str:
        """生成初始化代码（使用generators模块）"""
        generator = InitGenerator(self.config_data, self.chip_name, self.header_file_name)
        return generator.generate()
    
    def _generate_gpio_init_1521(self) -> List[str]:
        """生成 JZ8P1521 的 GPIO 初始化代码"""
        code = []
        gpio_config = self.config_data["gpio"]

        # P5有4个引脚 (P50-P53)，P6有8个引脚 (P60-P67)
        p5_dir = gpio_config["P5"]["direction"][:4]
        p6_dir = gpio_config["P6"]["direction"]
        p5_pullup = gpio_config["P5"]["pullup"][:4]
        p6_pullup = gpio_config["P6"]["pullup"]
        p5_pulldown = gpio_config["P5"]["pulldown"][:4]
        p6_pulldown = gpio_config["P6"]["pulldown"]
        p6_wakeup = gpio_config["P6"]["wakeup"]

        # 1. 方向控制寄存器 (0=输出, 1=输入)
        p5cr_val = self._calculate_port_control(p5_dir)
        p6cr_val = self._calculate_port_control(p6_dir)

        # 2. 上拉/下拉寄存器 (0=使能, 1=禁止)
        # IOC9/PHDCR: bit7-4 -> P6<7:4>下拉, bit3-0 -> P5<3:0>上拉
        p6pd_high = self._calculate_port_pull(p6_pulldown[4:8])
        p5ph_low = self._calculate_port_pull(p5_pullup)
        phdcr_val = (p6pd_high << 4) | p5ph_low

        # IOCB/PDCR: bit6-4 -> P6<2:0>下拉, bit3-0 -> P5<3:0>下拉
        p6pd_low = self._calculate_port_pull(p6_pulldown[0:3]) # P6.3没有下拉
        p5pd_low = self._calculate_port_pull(p5_pulldown)
        pdcr_val = (p6pd_low << 4) | p5pd_low

        # IOCD/PHCR: bit7-0 -> P6<7:0>上拉
        phcr_val = self._calculate_port_pull(p6_pullup)

        # 3. 唤醒使能寄存器 (0=禁止, 1=使能)
        # RD/ICIECR: P6口状态变化唤醒使能
        iciecr_val = self._calculate_port_pull(p6_wakeup, invert=True)

        # 生成代码
        code.append(f"\tPORT5=0x00;")
        code.append(f"\tPORT6=0x00;")
        code.append("")

        # 使用IOCP_W宏进行寄存器写操作
        self._add_code_with_comment(code, f'\tIOCP_W(P5CR, 0x{p5cr_val:02X});', "P5口设为输出; 0输出, 1输入")
        self._add_code_with_comment(code, f'\tIOCP_W(P6CR, 0x{p6cr_val:02X});', "P6口设为输出; 0输出, 1输入")
        code.append("")

        self._add_code_with_comment(code, f'\tIOCP_W(PHDCR, 0x{phdcr_val:02X});', "端口上下拉控制; bit7-4对应P67-P64下拉; bit3-bit0对应P53-P50上拉")
        self._add_code_with_comment(code, f'\tIOCP_W(PDCR, 0x{pdcr_val:02X});', "端口下拉控制; bit6-4对应P62-P60, bit3-bit0对应P53-P50")
        self._add_code_with_comment(code, f'\tIOCP_W(PHCR, 0x{phcr_val:02X});', "P6端口上拉控制; bit7-bit0对应P67-P60, 0使能, 1禁止")
        code.append("")

        self._add_comment(code, "-----端口变化中断唤醒------")
        self._add_code_with_comment(code, f'\tICIECR = 0x{iciecr_val:02X};', "P6口状态变化唤醒使能; 0禁止, 1使能")
        code.append("")

        return code
    
    def _generate_gpio_init_2615(self) -> List[str]:
        """生成 JZ8P2615 的 GPIO 初始化代码"""
        code = []
        gpio_config = self.config_data["gpio"]
        
        # 计算寄存器值
        p5con = self._calculate_port_control(gpio_config["P5"]["direction"])
        p6con = self._calculate_port_control(gpio_config["P6"]["direction"])
        p5ph = self._calculate_port_pull(gpio_config["P5"]["pullup"])
        p6ph = self._calculate_port_pull(gpio_config["P6"]["pullup"])
        p5pd = self._calculate_port_pull(gpio_config["P5"]["pulldown"])
        p6pd = self._calculate_port_pull(gpio_config["P6"]["pulldown"])
        p6od = self._calculate_port_pull(gpio_config["P6"].get("opendrain", [0]*8), invert=True)
        p6wd = self._calculate_port_pull(gpio_config["P6"].get("weakdrive", [0]*8), invert=True)
        p5iwe = self._calculate_port_pull(gpio_config["P5"].get("wakeup", [0]*8), invert=True)
        p6iwe = self._calculate_port_pull(gpio_config["P6"].get("wakeup", [0]*8), invert=True)
        
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
        wdt_config = self.config_data.get("system", {}).get("wdt", {})
        timer_config = self.config_data.get("timer", {})

        # --- IOCE/WDE (看门狗控制寄存器) ---
        # Bit7=WDTEN, Bit6=EIS (P60外部中断使能)
        wdten = 0x80 if wdt_config.get("enabled") else 0x00
        eis = 0x40 if interrupt_config.get("int0_enabled") else 0x00
        
        # 根据数据手册，复位值为 1011 1111 (0xBF)。保留位为1
        ioce_value = 0x3F | wdten | eis
        
        self._add_comment(code, "-----WDT及外部中断设置------")
        self._add_code_with_comment(code, f'\tIOCP_W(WDE, 0x{ioce_value:02X});', "WDT控制及外部中断使能; Bit7=WDTEN, Bit6=EIS(P60)")
        code.append("")

        # --- IOCF/RIEN (中断使能控制寄存器) ---
        # Bit3=T1IE, Bit2=EXIE, Bit1=ICIE, Bit0=TCIE
        iocf_value = 0x00
        
        # T1/PWM 中断 (T1IE)
        pwm_enabled = any(self.config_data["pwm"].get(p, {}).get("enabled") for p in ["PWM1", "PWM2", "PWM3"])
        if pwm_enabled:
            iocf_value |= 0x08

        # 外部中断 (EXIE)
        if interrupt_config.get("int0_enabled"):
            iocf_value |= 0x04

        # P6 端口状态改变中断 (ICIE)
        if interrupt_config.get("port_change", {}).get("P6"):
            iocf_value |= 0x02

        # TCC 中断 (TCIE)
        if timer_config.get("TCC", {}).get("interrupt"):
            iocf_value |= 0x01

        self._add_code_with_comment(code, f'\tIOCP_W(RIEN, 0x{iocf_value:02X});', "中断使能控制; T1IE,EXIE,ICIE,TCIE")
        code.append("")

        # --- RF/RIFG (中断标志寄存器) ---
        self._add_comment(code, "-----清中断标志-----")
        self._add_code_with_comment(code, f"\tRF = 0x00;", "清所有中断标志位")
        code.append("")

        return code
    
    def _generate_interrupt_init_2615(self) -> List[str]:
        """生成 JZ8P2615 的中断初始化代码"""
        code = []
        wdtcon = compute_wdtcon_value(self.config_data["interrupt"])
        inte0 = compute_inte0_value(self.config_data["interrupt"])
        inte1 = compute_inte1_value(self.config_data["interrupt"])
        
        self._add_comment(code, " -----使能外部中断设置------")
        self._add_code_with_comment(code, f"\tWDTCON=0x{wdtcon:02X};", "bit6&5:P60&P53外部中断功能控制位，0:普通IO口, 1:外部中断口")
        code.append("")
        self._add_code_with_comment(code, f"\tINTE0=0x{inte0:02X};", "中断使能")
        self._add_code_with_comment(code, f"\tINTE1=0x{inte1:02X};", "周期及占空比中断")
        self._add_code_with_comment(code, f"\tINTF0=0x00;", "清中断标志位")
        code.append(f"\tINTF1=0x00;")
        code.append("")
        
        return code
    
    def _calculate_port_control(self, direction_list):
        """计算端口控制寄存器值（使用utils模块）"""
        return calculate_port_control(direction_list)
    
    def _calculate_port_pull(self, pull_list, invert=False):
        """计算上拉/下拉寄存器值（使用utils模块）"""
        return calculate_port_pull(pull_list, invert)
    
    def _generate_tcc_init_code(self):
        """生成TCC定时器初始化代码（JZ8P1521）"""
        code = []
        config = self.config_data["timer"]["TCC"]
        code.append("void file_tcc_Init(void)")
        code.append("{")
        self._add_comment(code, "===========TCC初始化==============")
        
        # CONT寄存器计算（IOPAGE-CONT）
        # Bit7=RTCS, Bit6=INT, Bit5=TS, Bit4=TE, Bit3=PAB, Bit2:0=PSR<2:0>
        cont_value = 0x3F  # 默认值
        # PSR分频设置
        prescaler_val = config["prescaler"] & 0x07
        prescaler_map = {0: "1:2", 1: "1:4", 2: "1:8", 3: "1:16", 
                         4: "1:32", 5: "1:64", 6: "1:128", 7: "1:256"}
        cont_value = (cont_value & 0xF8) | prescaler_val
        
        # PAB位 (bit 3): 0=分给TCC, 1=分给WDT
        # 这里默认分给TCC，所以PAB=0
        
        # TE位 (bit 4): 边沿选择
        if config.get("edge", "rising") == "falling":
            cont_value |= 0x10  # TE=1
        
        # TS位 (bit 5): 信号源选择
        if config["clock_source"] == "external":
            cont_value |= 0x20  # TS=1
        
        # INT位 (bit 6): 中断使能标志位（全局中断）
        # 这里不设置，由用户程序控制
        
        # RTCS位 (bit 7): RTC选择（如果使用RTC）
        # 这里不设置
        
        self._add_comment(code, "-----切换到IOPAGE页面-----")
        code.append("\tIOPAGE = 0x01;  // 切换到IOPAGE页面")
        comment = f"控制寄存器 (PSR={prescaler_val}, 分频={prescaler_map[prescaler_val]})"
        self._add_code_with_comment(code, f"\tCONT = 0x{cont_value:02X};", comment)
        code.append("")
        
        # TCC计数寄存器（RPAGE-R1）
        self._add_comment(code, "-----切换到RPAGE页面-----")
        code.append("\tRPAGE = 0x00;  // 切换到RPAGE页面")
        self._add_code_with_comment(code, f"\tR1 = {config['count_value']};", "TCC计数寄存器")
        
        # TCC时钟源选择（RE寄存器，CPUCON）
        if config["clock_source"] == "system":
            # 需要设置RE寄存器的TCCCKS位（Bit5）
            code.append("")
            self._add_code_with_comment(code, f"\tRE |= 0x20;", "TCC时钟源选择系统时钟")
        
        if config["interrupt"]:
            # 中断使能在IOCF寄存器中设置（已在中断初始化中处理）
            pass
        
        code.append("}")
        code.append("")
        
        return code
    
    def _generate_tc0_init_code(self):
        """生成TC0初始化代码"""
        code = []
        config = self.config_data["timer"]["TC0"]
        code.append("void file_tc0_Init(void)")
        code.append("{")
        self._add_comment(code, "===========TC0初始化==============")
        
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
        
        comment = f"TC0控制寄存器 (TCOPSR={prescaler_val}, 分频={prescaler_map[prescaler_val]})"
        self._add_code_with_comment(code, f"\tTC0CON = 0x{tc0con:02X};", comment)
        self._add_code_with_comment(code, f"\tTC0C = {config['count_value']};", "TC0计数寄存器")
        
        if config["interrupt"]:
            self._add_code_with_comment(code, f"\tINTE0 |= 0x01;", "中断使能")
        
        code.append("}")
        code.append("")
        return code
    
    def _generate_tc1_init_code(self):
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
    
    def _generate_tc2_init_code(self):
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
    
    def _generate_adc_init_code(self):
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
        
        adcon1 = 0x40  # ADEN=1
        if config["calibration"]:
            adcon1 |= 0x10  # CALI=1
        self._add_code_with_comment(code, f"\tADCON1 = 0x{adcon1:02X};", "AD使能")
        code.append("}")
        code.append("")
        return code
    
    def _generate_pwm_init_code(self):
        """生成PWM初始化代码"""
        code = []
        code.append("void file_pwm_Init(void)")
        code.append("{")
        self._add_comment(code, "===========PWM初始化==============")
        pwm_config = self.config_data["pwm"]
        
        if self._is_chip_1521():
            # JZ8P1521: 3路PWM，共周期
            pwm_list = ["PWM1", "PWM2", "PWM3"]
            
            # 检查是否有PWM使能
            pwm_enabled_list = []
            for pwm_name in pwm_list:
                if pwm_config.get(pwm_name, {}).get("enabled", False):
                    pwm_enabled_list.append(pwm_name)

            if not pwm_enabled_list:
                # 如果没有PWM使能，则不生成任何代码
                return []

            # 计算PWMCON寄存器（RPAGE-R8）
            # Bit7=T1EN, Bit6=PWM3EN, Bit5=PWM2EN, Bit4=PWM1EN, Bit3=T1PTEN, Bit2:0=T1P<2:0>
            pwmmcon = 0x00
            
            # 设置T1EN（Bit7）
            pwmmcon |= 0x80
            
            # 设置各个PWM使能位
            if "PWM1" in pwm_enabled_list:
                pwmmcon |= 0x10  # Bit4
            if "PWM2" in pwm_enabled_list:
                pwmmcon |= 0x20  # Bit5
            if "PWM3" in pwm_enabled_list:
                pwmmcon |= 0x40  # Bit6
            
            # 获取第一个PWM的配置作为共周期配置
            first_pwm = pwm_enabled_list[0]
            first_config = pwm_config[first_pwm]
            
            # T1预分频设置（Bit3:0）
            prescaler = first_config.get("prescaler", 0) & 0x07
            if prescaler > 0:
                pwmmcon |= 0x08  # T1PTEN=1
                pwmmcon |= prescaler  # T1P<2:0>
            
            # 切换到RPAGE页面
            self._add_comment(code, "-----切换到RPAGE页面-----")
            code.append("\tRPAGE = 0x00;  // 切换到RPAGE页面")
            code.append("")
            
            # PWM控制寄存器
            self._add_code_with_comment(code, f"\tR8 = 0x{pwmmcon:02X};", "PWM控制寄存器\t;T1EN,PWM3EN,PWM2EN,PWM1EN,T1PTEN")
            
            # PWM周期寄存器（R9）- 共周期
            period = first_config.get("period", 100) & 0xFF
            self._add_code_with_comment(code, f"\tR9 = {period};", f"PWM周期寄存器\t;共周期={period}")
            code.append("")
            
            # 各个PWM占空比寄存器
            pdc_map = {"PWM1": "RA", "PWM2": "RB", "PWM3": "RC"}
            for pwm_name in pwm_enabled_list:
                duty = pwm_config[pwm_name].get("duty", 0) & 0xFF
                reg_name = pdc_map[pwm_name]
                self._add_code_with_comment(code, f"\t{reg_name} = {duty};", f"{pwm_name}占空比\t;占空比={duty}")
            
            # PWM时钟源和互补输出（RE寄存器，CPUCON）
            code.append("")
            if first_config.get("clock_source") == "system":
                self._add_code_with_comment(code, f"\tRE |= 0x40;", "PWM时钟源选择系统时钟")
            
            if pwm_config.get("PWM1", {}).get("invert", False):
                self._add_code_with_comment(code, f"\tRE |= 0x80;", "PWM1互补输出")
        else:
            # JZ8P2615: 4路PWM
            for pwm_name in ["PWM1", "PWM2", "PWM3", "PWM4"]:
                if pwm_config.get(pwm_name, {}).get("enabled", False):
                    comment = f"{pwm_name}配置: 周期={pwm_config[pwm_name]['period']}, 占空比={pwm_config[pwm_name]['duty']}"
                    self._add_comment(code, comment)
        
        code.append("}")
        code.append("")
        return code
    
    def generate_main_code(self) -> str:
        """生成主程序代码（使用generators模块）"""
        generator = MainGenerator(self.config_data, self.chip_name, self.header_file_name)
        return generator.generate()
    
    def generate_all_files(self) -> Dict[str, str]:
        """生成所有文件（C文件和H文件）"""
        files = {}
        
        # 生成init.c和init.h（1521使用user.c和user.h）
        if self._is_chip_1521():
            files["user.c"] = self.generate_init_code()
            files["user.h"] = self.generate_init_header()
        else:
            files["init.c"] = self.generate_init_code()
            files["init.h"] = self.generate_init_header()
        
        # 生成isr.c
        files["isr.c"] = self.generate_isr_code()

        # 睡眠代码
        if self.config_data.get("sleep", {}).get("enabled"):
            # 根据芯片类型决定文件名
            if self._is_chip_1521():
                files["sleep.c"] = self.generate_sleep_code()
                files["sleep.h"] = self.generate_sleep_header()
            else:
                files["sleep.c"] = self.generate_sleep_code()
                files["sleep.h"] = self.generate_sleep_header()

        # 生成main.c和main.h（基础模板）
        files["main.c"] = self.generate_main_code()
        files["main.h"] = self.generate_main_header()
        
        # 如果启用 ADC，生成 ADC.C / ADC.H
        if self.config_data.get("adc", {}).get("enabled"):
            files["ADC.C"] = self.generate_adc_code()
            files["ADC.H"] = self.generate_adc_header()
        
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
        if self._is_chip_1521():
            # JZ8P1521格式
            code.append("#ifndef _PWM_H_")
            code.append("#define _PWM_H_")
            code.append("")
            code.append("#include \"user.h\"")
            code.append("enum")
            code.append("{")
            code.append("    E_PWM_DIV_1 = 0x00,")
            code.append("    E_PWM_DIV_2 = 0X08,")
            code.append("    E_PWM_DIV_4,")
            code.append("    E_PWM_DIV_8,")
            code.append("    E_PWM_DIV_16,")
            code.append("    E_PWM_DIV_32,")
            code.append("    E_PWM_DIV_64,")
            code.append("    E_PWM_DIV_128,")
            code.append("    E_PWM_DIV_256,")
            code.append("};")
            code.append("#define    D_PWM_DIV_SLCT     E_PWM_DIV_1    // PWM分频选择")
            code.append("")
            channel_order = [("PWM1", "pwm1Init"), ("PWM2", "pwm2Init"), ("PWM3", "pwm3Init")]
        else:
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
                code.append(f"void {func_name}();")
        code.append("#endif")
        code.append("")
        return "\n".join(code)

    def generate_pwm_code(self) -> str:
        """生成 pwm.c 源文件（使用generators模块）"""
        generator = PWMGenerator(self.config_data, self.chip_name, self.header_file_name)
        return generator.generate()

    def generate_main_header(self) -> str:
        """生成main.h头文件"""
        code = []
        if self._is_chip_1521():
            # JZ8P1521格式：只包含user.h
            code.append("#ifndef _MAIN_H_")
            code.append("#define _MAIN_H_")
            code.append("")
            code.append("#include \"user.h\"")
            code.append("")
            code.append("#endif ")
        else:
            # JZ8P2615格式
            code.append("#ifndef __MAIN_H__")
            code.append("#define __MAIN_H__")
            code.append("")
            code.append(f"#include \"{self.header_file_name}\"")
            code.append("#include \"type.h\"")
            code.append("")
            # 根据配置添加定时器计数常量
            if "TC0" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC0"].get("enabled", False):
                count_val = self.config_data["timer"]["TC0"]["count_value"]
                code.append(f"#define\tTCC_NUM\t{count_val}")
                code.append("")
            
            # 添加GPIO定义（根据配置）
            gpio_defs = []
            gpio_config = self.config_data["gpio"]
            
            # 检查P5端口配置，生成定义
            p5_pin_count = len(gpio_config["P5"]["direction"])
            for pin in range(p5_pin_count):
                if gpio_config["P5"]["direction"][pin] == 0:  # 输出
                    gpio_defs.append(f"#define\tIo_P5{pin}\t\tPORT5_{pin}")
            
            # 检查P6端口配置，生成定义
            p6_pin_count = len(gpio_config["P6"]["direction"])
            for pin in range(p6_pin_count):
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
        
        return "\n".join(code)
    
    def generate_isr_code(self) -> str:
        """生成isr.c代码（使用generators模块）"""
        generator = ISRGenerator(self.config_data, self.chip_name, self.header_file_name)
        return generator.generate()
    
    def generate_sleep_code(self) -> str:
        """生成sleep.c代码（使用generators模块）"""
        generator = SleepGenerator(self.config_data, self.chip_name, self.header_file_name)
        return generator.generate()
    
    def generate_sleep_header(self) -> str:
        """生成睡眠功能头文件"""
        code = []
        if self._is_chip_1521():
            # JZ8P1521 格式：生成sleep.h
            code.append("#ifndef _SLEEP_H_")
            code.append("#define _SLEEP_H_")
            code.append("")
            code.append("#include \"user.h\"")
            code.append("")
            code.append("")
            code.append("void fw_sleepEvent();")
            code.append("#endif")
        else:
            # 其他芯片格式
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
        # 优先使用从示例项目加载的模板
        if self.type_header_template:
            return self.type_header_template
        
        # 如果没有模板，根据芯片类型生成默认格式
        if self._is_chip_1521():
            # JZ8P1521 格式（与示例项目一致）
            return (
                "#ifndef _TYPE_H_\n"
                "#define _TYPE_H_\n"
                "\n"
                f"#include \"{self.header_file_name.lower()}\"\n"
                "\n"
                "//************************************/\n"
                "//-----------指令定义---------------- \n"
                "//************************************/\n"
                "\n"
                "#define EI()  __asm__(\" ei \")\n"
                "#define DI()  __asm__(\" di \")\n"
                "#define NOP() __asm__(\" nop \")\n"
                "#define CWDT() __asm__(\" CWDT \")\n"
                "#define SLEEP() __asm__(\" sleep \")\n"
                "/************************************/\n"
                "//-----------寄存器读写示例----------  \n"
                "/************************************/\n"
                "#define CONTW(VAL)\t\t\t__asm__(\"mov a,@\"#VAL\"\\n ctw\")\t\t\t//CTW = VAL：CONT寄存器赋值\n"
                "#define IOCP_W(REG,VAL)\t\t__asm__(\"mov a,@\"#VAL\"\\n iw \"#REG)\t\t//REG = VAL：IOC页寄存器赋值\n"
                "#define IOCP_R(RAM,REG)\t\t__asm__(\"ir \"#REG\"\\n mov \"#RAM\",a\")\t\t//RAM = REG：IOC页寄存器读值\n"
                "#define PUSH(A_REG,R3_REG)\t__asm__(\"mov \"#A_REG\",a\\n swap \"#A_REG\"\\n swapa STATUS\\n mov \"#R3_REG\",a\")\t//中断入栈保护\t\n"
                "#define POP(A_REG,R3_REG)\t__asm__(\"swapa \"#R3_REG\"\\n mov STATUS,a\\n swapa \"#A_REG)\n"
                "\n"
                "\n"
                "#define IOCP_W_AND(REG,VAL) __asm__(\"ir \"#REG\"\\n and a,@\"#VAL\"\\n iw \"#REG)  // & 与\n"
                "#define IOCP_W_OR(REG,VAL)  __asm__(\"ir \"#REG\"\\n or a,@\"#VAL\"\\n iw \"#REG)   // | 或\n"
                "\n"
                "//************************************/\n"
                "//-----------  重定义 ---------------- \n"
                "//************************************/\n"
                "typedef   unsigned char\t\tuint8_t;\n"
                "typedef   unsigned int \t\tuint16_t;\n"
                "\n"
                "#define   ENABLE    1\n"
                "#define   DISABLE   0\n"
                "\n"
                "#endif\n"
            )
        else:
            # JZ8P2615 格式（默认）
            return (
            "#ifndef _TYPE_H_\n"
            "#define _TYPE_H_\n"
            "\n"
            f"#include \"{self.header_file_name}\"\n"
                "\n"
                "\n"
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
    
    # 注意：_compute_wdtcon_value, _compute_inte0_value, _compute_inte1_value 方法
    # 已迁移到 utils.register_calc 模块，直接使用 compute_wdtcon_value 等函数
    
    def generate_init_header(self) -> str:
        """生成init.h头文件（1521生成user.h）"""
        code = []
        if self._is_chip_1521():
            # JZ8P1521格式：生成user.h
            code.append("#ifndef _USER_H_")
            code.append("#define _USER_H_")
            code.append("")
            code.append("#include \"type.h\"")
            code.append("#include \"pwm.h\"")
            if self.config_data.get("sleep", {}).get("enabled"):
                code.append("#include \"sleep.h\"")
            code.append("")
            code.append("")
            code.append("/*********** 数据定义 ***************/")
            code.append("#define   T_1MS             6")
            code.append("#define   TCC_TIM           T_1MS")
            code.append("")
            code.append("#define   D_10MS            1")
            code.append("")
            code.append("")
            code.append("/*********** 端口定义 ***************/")
            code.append("#define   IO_KEY        PORT6_4")
            code.append("")
            code.append("/*********** 标志位定义 *************/")
            code.append("typedef struct SYS_FlgBit_")
            code.append("{   ")
            code.append("    uint8_t BIT0:1;              // 10ms")
            code.append("    uint8_t BIT1:1;")
            code.append("    uint8_t BIT2:1;")
            code.append("    uint8_t BIT3:1;")
            code.append("    uint8_t BIT4:1;")
            code.append("    uint8_t BIT5:1;")
            code.append("    uint8_t BIT6:1;")
            code.append("    uint8_t BIT7:1;")
            code.append("}SYS_FlgBit;")
            code.append("typedef union SYS_FlgBitClass_")
            code.append("{")
            code.append("    uint8_t       FlgAll;")
            code.append("    SYS_FlgBit    SYS_Flg;")
            code.append("}SYS_FlgBitClass;")
            code.append("")
            code.append("extern SYS_FlgBitClass U_Flage;")
            code.append("#define    Time_10ms          (U_Flage.SYS_Flg.BIT0) ")
            code.append("#define    F_CHARGE        (U_Flage.SYS_Flg.BIT1) ")
            code.append("#define    F_CHARGE_FULL   (U_Flage.SYS_Flg.BIT2) ")
            code.append("#define    F_CHARGE_H_IO   (U_Flage.SYS_Flg.BIT3) ")
            code.append("#define    dir			   (U_Flage.SYS_Flg.BIT4) ")
            code.append("")
            code.append("/*********** 寄存器*************/")
            code.append("extern uint8_t r_g_workMod;")
            code.append("")
            code.append("/*********** 函数 *************/")
            code.append("void fw_clrRam(void);")
            code.append("void fw_gpioInit(void);")
            if "TCC" in self.config_data.get("timer", {}) and self.config_data["timer"]["TCC"]["enabled"]:
                code.append("void fw_tc0Init(void);")
            code.append("")
            code.append("#endif")
            code.append("")
        else:
            # JZ8P2615格式：生成init.h
            code.append("#ifndef __INIT_H__")
            code.append("#define __INIT_H__")
            code.append("")
            code.append("void file_clrRam(void);")
            code.append("void file_init(void);")
            code.append("")
        
        # 根据配置添加初始化函数声明
            if "TC0" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC0"]["enabled"]:
                code.append("void file_tc0_Init(void);")
            if "TC1" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC1"]["enabled"]:
                code.append("void file_tc1_Init(void);")
            if "TC2" in self.config_data.get("timer", {}) and self.config_data["timer"]["TC2"]["enabled"]:
                code.append("void file_tc2_Init(void);")
        
            if self.config_data.get("adc", {}).get("enabled", False):
                code.append("void file_adc_Init(void);")
        
            pwm_list = ["PWM1", "PWM2", "PWM3", "PWM4"]
            pwm_enabled = any(
            self.config_data.get("pwm", {}).get(p, {}).get("enabled", False) 
            for p in pwm_list
        )
            if pwm_enabled:
                code.append("void file_pwm_Init(void);")
            
            code.append("")
            code.append("#endif")
        code.append("")
        
        return "\n".join(code)
    
    def generate_adc_code(self) -> str:
        """生成ADC.C文件（使用generators模块）"""
        generator = ADCGenerator(self.config_data, self.chip_name, self.header_file_name)
        return generator.generate()
    
    def generate_adc_header(self) -> str:
        """生成ADC.H头文件"""
        code = []
        code.append("#ifndef _FW_ADC_H_")
        code.append("#define _FW_ADC_H_")
        code.append("")
        code.append("#include \"type.h\"")
        code.append("")
        self._add_comment(code, "ADC数据定义")
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
        self._add_code_with_comment(code, "\tE_Vrefh_VDD = 0,", "ADC reference high voltage is VDD")
        self._add_code_with_comment(code, "\tE_Vrefh_4V,", "ADC reference high voltage is 4V")
        self._add_code_with_comment(code, "\tE_Vrefh_3V,", "ADC reference high voltage is 3V")
        self._add_code_with_comment(code, "\tE_Vrefh_2V,", "ADC reference high voltage is 2V")
        self._add_code_with_comment(code, "\tE_Vrefh_1_5V,", "ADC reference high voltage is 1.5V")
        code.append("};")
        self._add_code_with_comment(code, "#define\tC_Ckl_Div16\t\t0x00", "ADC clock is Fosc/16")
        self._add_code_with_comment(code, "#define\tC_Ckl_Div4\t\t0x40", "ADC clock is Fosc/4")
        self._add_code_with_comment(code, "#define\tC_Ckl_Div64\t\t0x80", "ADC clock is Fosc/64")
        self._add_code_with_comment(code, "#define\tC_Ckl_Div1\t\t0xC0", "ADC clock is Fosc/1")
        code.append("")
        self._add_code_with_comment(code, "#define\tC_ADC_START\t\t0x40", "ADC Start")
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

