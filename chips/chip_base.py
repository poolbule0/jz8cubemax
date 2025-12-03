#!/usr/bin/env python
# -*- coding: gbk -*-
"""
芯片抽象基类
定义所有芯片必须实现的接口
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
import os


class ChipBase(ABC):
    """芯片抽象基类 - 所有芯片实现必须继承此类"""
    
    def __init__(self):
        """初始化芯片"""
        self.chip_name = self.get_chip_name()
        self.chip_display_name = self.get_display_name()
        self.datasheet_path = self.get_datasheet_path()
        self.example_path = self.get_example_path()
        self.header_file_name = self.get_header_file_name()
        self.register_map = {}
        self._load_register_map()
    
    @abstractmethod
    def get_chip_name(self) -> str:
        """
        返回芯片的唯一标识名称（用于内部识别）
        例如: "JZ8P2615"
        """
        pass
    
    @abstractmethod
    def get_display_name(self) -> str:
        """
        返回芯片的显示名称（用于UI显示）
        例如: "JZ8P2615"
        """
        pass
    
    @abstractmethod
    def get_datasheet_path(self) -> str:
        """
        返回数据手册文件路径（相对于项目根目录）
        例如: "JZ8P2615-V1.3.md"
        """
        pass
    
    @abstractmethod
    def get_example_path(self) -> str:
        """
        返回示例项目目录路径（相对于项目根目录）
        例如: "示例项目"
        """
        pass
    
    @abstractmethod
    def get_header_file_name(self) -> str:
        """
        返回芯片头文件名
        例如: "JZ8P2615.h"
        """
        pass
    
    @abstractmethod
    def get_default_config(self) -> Dict[str, Any]:
        """
        返回该芯片的默认配置
        不同芯片的寄存器、功能模块可能不同
        """
        pass
    
    def _load_register_map(self):
        """加载寄存器映射表"""
        header_file = os.path.join(self.example_path, self.header_file_name)
        if not os.path.exists(header_file):
            print(f"警告: 头文件不存在: {header_file}")
            return
        
        try:
            content = self._read_file_with_encoding(header_file)
            self.register_map = self._parse_register_map(content)
            print(f"芯片 {self.chip_display_name} 寄存器映射表加载成功，共 {len(self.register_map)} 个寄存器")
        except Exception as e:
            print(f"解析寄存器映射表失败: {e}")
    
    def _parse_register_map(self, content: str) -> Dict[str, Any]:
        """
        解析寄存器映射表
        子类可以重写此方法以实现不同的解析逻辑
        """
        import re
        register_map = {}
        
        # 默认解析格式: #define REG_NAME_ADDR 0xXXX
        pattern = r'#define\s+(\w+_ADDR)\s+0X([0-9A-F]+)'
        matches = re.findall(pattern, content, re.IGNORECASE)
        
        for reg_name, addr in matches:
            reg_base_name = reg_name.replace('_ADDR', '')
            register_map[reg_base_name] = {
                'address': int(addr, 16),
                'name': reg_base_name
            }
        
        return register_map
    
    def _read_file_with_encoding(self, filepath: str) -> str:
        """读取文件，尝试多种编码"""
        encodings = ['gbk', 'utf-8', 'gb2312', 'latin-1']
        for encoding in encodings:
            try:
                with open(filepath, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        raise ValueError(f"无法读取文件: {filepath}")
    
    def get_register_map(self) -> Dict[str, Any]:
        """获取寄存器映射表"""
        return self.register_map
    
    def get_available_modules(self) -> List[str]:
        """
        返回该芯片支持的功能模块列表
        例如: ["gpio", "adc", "timer", "pwm", "interrupt", "sleep"]
        """
        config = self.get_default_config()
        return list(config.keys())
    
    def validate_config(self, config: Dict[str, Any]) -> tuple[bool, List[str]]:
        """
        验证配置是否适用于该芯片
        返回: (是否有效, 错误列表)
        """
        errors = []
        # 子类可以实现具体的验证逻辑
        return len(errors) == 0, errors

