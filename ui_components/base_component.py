#!/usr/bin/env python
# -*- coding: gbk -*-
"""
UI组件基类
提供所有UI组件的通用功能
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from control import ConfigController


class BaseComponent:
    """UI组件基类"""
    
    def __init__(self, controller: 'ConfigController', parent: tk.Widget):
        """
        初始化组件
        
        Args:
            controller: 配置控制器
            parent: 父组件
        """
        self.controller = controller
        self.parent = parent
    
    def _is_chip_1521(self) -> bool:
        """判断当前芯片是否为 JZ8P1521"""
        chip_name = getattr(self.controller, 'chip_name', 'JZ8P2615')
        return chip_name == "JZ8P1521"
    
    def _get_config_safe(self, *keys, default=None):
        """
        安全获取配置值，如果键不存在则返回默认值
        
        Args:
            *keys: 配置键路径，如 "timer", "TC0", "enabled"
            default: 默认值
            
        Returns:
            配置值或默认值
        """
        config = self.controller.get_config()
        try:
            value = config
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default

