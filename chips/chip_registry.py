#!/usr/bin/env python
# -*- coding: gbk -*-
"""
芯片注册表
管理所有可用的芯片实现
"""

from typing import Dict, Optional, List
from .chip_base import ChipBase
from .jz8p2615 import JZ8P2615Chip
from .jz8p1521 import JZ8P1521


class ChipRegistry:
    """芯片注册表 - 单例模式"""
    
    _instance = None
    _chips: Dict[str, ChipBase] = {}
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChipRegistry, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._register_default_chips()
            ChipRegistry._initialized = True
    
    def _register_default_chips(self):
        """注册默认芯片"""
        # 注册 JZ8P2615
        jz8p2615 = JZ8P2615Chip()
        self.register_chip(jz8p2615)
        # 注册 JZ8P1521
        jz8p1521 = JZ8P1521()
        self.register_chip(jz8p1521)
    
    def register_chip(self, chip: ChipBase):
        """注册一个芯片实现"""
        chip_name = chip.get_chip_name()
        self._chips[chip_name] = chip
        print(f"芯片 {chip.get_display_name()} ({chip_name}) 已注册")
    
    def get_chip(self, chip_name: str) -> Optional[ChipBase]:
        """根据芯片名称获取芯片实例"""
        return self._chips.get(chip_name)
    
    def get_all_chips(self) -> Dict[str, ChipBase]:
        """获取所有已注册的芯片"""
        return self._chips.copy()
    
    def get_chip_names(self) -> List[str]:
        """获取所有芯片名称列表"""
        return list(self._chips.keys())
    
    def get_chip_display_names(self) -> Dict[str, str]:
        """获取芯片名称到显示名称的映射"""
        return {name: chip.get_display_name() 
                for name, chip in self._chips.items()}
    
    def get_default_chip(self) -> Optional[ChipBase]:
        """获取默认芯片（通常是第一个注册的）"""
        if self._chips:
            return list(self._chips.values())[0]
        return None

