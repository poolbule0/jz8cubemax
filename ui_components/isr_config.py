#!/usr/bin/env python
# -*- coding: gbk -*-
"""
ISR配置UI组件
提供ISR配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class ISRConfigComponent(BaseComponent):
    """ISR配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建ISR配置界面
        
        Args:
            parent: 父组件
        """
        cfg = self.controller.get_config()["isr"]
        
        ttk.Label(parent, text="isr.c - 中断服务程序配置",
                  font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(5, 10))
        
        content_frame = ttk.Frame(parent)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # 10ms计时配置
        block1 = ttk.LabelFrame(content_frame, text="10ms计数配置", padding="10")
        block1.pack(fill=tk.X, padx=5, pady=5)
        
        t10_enable_var = tk.BooleanVar(value=cfg["enable_time_10ms"])
        ttk.Checkbutton(block1, text="启用10ms计时", variable=t10_enable_var,
                        command=lambda: self._update_isr_config("enable_time_10ms", t10_enable_var.get())
                        ).grid(row=0, column=0, sticky=tk.W)
        
        # 计数变量名
        ttk.Label(block1, text="计数变量名:").grid(row=1, column=0, sticky=tk.W, pady=2)
        t10_reg_var = tk.StringVar(value=cfg.get("reg_10ms_name", "reg_10ms"))
        ttk.Entry(block1, textvariable=t10_reg_var, width=20).grid(row=1, column=1, sticky=tk.W, pady=2)
        t10_reg_var.trace_add("write",
                              lambda *args: self._update_isr_config("reg_10ms_name", t10_reg_var.get()))
        
        ttk.Label(block1, text="阈值:").grid(row=2, column=0, sticky=tk.W, pady=2)
        t10_threshold_var = tk.IntVar(value=cfg["time_10ms_threshold"])
        t10_spin = ttk.Spinbox(block1, from_=1, to=1000, width=10,
                               textvariable=t10_threshold_var)
        t10_spin.grid(row=2, column=1, sticky=tk.W, pady=2)
        t10_threshold_var.trace_add("write",
                                    lambda *args: self._update_isr_int_var("time_10ms_threshold", t10_threshold_var))
        
        ttk.Label(block1, text="标志变量:").grid(row=3, column=0, sticky=tk.W, pady=2)
        t10_flag_var = tk.StringVar(value=cfg["time_10ms_flag"])
        ttk.Entry(block1, textvariable=t10_flag_var, width=20).grid(row=3, column=1, sticky=tk.W, pady=2)
        t10_flag_var.trace_add("write",
                               lambda *args: self._update_isr_config("time_10ms_flag", t10_flag_var.get()))
        
        # 200us计时配置
        block2 = ttk.LabelFrame(content_frame, text="200us计数配置", padding="10")
        block2.pack(fill=tk.X, padx=5, pady=5)
        
        t200_enable_var = tk.BooleanVar(value=cfg["enable_time_200us"])
        ttk.Checkbutton(block2, text="启用200us计时", variable=t200_enable_var,
                        command=lambda: self._update_isr_config("enable_time_200us", t200_enable_var.get())
                        ).grid(row=0, column=0, sticky=tk.W)
        
        # 计数变量名
        ttk.Label(block2, text="计数变量名:").grid(row=1, column=0, sticky=tk.W, pady=2)
        t200_reg_var = tk.StringVar(value=cfg.get("reg_200us_name", "reg_200us"))
        ttk.Entry(block2, textvariable=t200_reg_var, width=20).grid(row=1, column=1, sticky=tk.W, pady=2)
        t200_reg_var.trace_add("write",
                               lambda *args: self._update_isr_config("reg_200us_name", t200_reg_var.get()))
        
        ttk.Label(block2, text="阈值:").grid(row=2, column=0, sticky=tk.W, pady=2)
        t200_threshold_var = tk.IntVar(value=cfg["time_200us_threshold"])
        t200_spin = ttk.Spinbox(block2, from_=1, to=1000, width=10,
                                textvariable=t200_threshold_var)
        t200_spin.grid(row=2, column=1, sticky=tk.W, pady=2)
        t200_threshold_var.trace_add("write",
                                     lambda *args: self._update_isr_int_var("time_200us_threshold", t200_threshold_var))
        
        ttk.Label(block2, text="标志变量:").grid(row=3, column=0, sticky=tk.W, pady=2)
        t200_flag_var = tk.StringVar(value=cfg["time_200us_flag"])
        ttk.Entry(block2, textvariable=t200_flag_var, width=20).grid(row=3, column=1, sticky=tk.W, pady=2)
        t200_flag_var.trace_add("write",
                                lambda *args: self._update_isr_config("time_200us_flag", t200_flag_var.get()))
    
    def _update_isr_config(self, key: str, value):
        """更新ISR配置"""
        self.controller.config_data["isr"][key] = value
    
    def _update_isr_int_var(self, key: str, var: tk.IntVar):
        """更新ISR整数配置"""
        self.controller.config_data["isr"][key] = var.get()

