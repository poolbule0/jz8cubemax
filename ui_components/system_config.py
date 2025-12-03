#!/usr/bin/env python
# -*- coding: gbk -*-
"""
系统配置UI组件
提供系统配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class SystemConfigComponent(BaseComponent):
    """系统配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建系统配置界面
        
        Args:
            parent: 父组件
        """
        # 系统配置通常比较简单，这里提供一个基础框架
        # 如果需要添加系统配置项，可以在这里扩展
        ttk.Label(parent, text="系统配置",
                  font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(5, 10))
        
        info_label = ttk.Label(parent, 
                              text="系统配置选项（待扩展）",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=20)

