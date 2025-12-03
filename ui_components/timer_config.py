#!/usr/bin/env python
# -*- coding: gbk -*-
"""
定时器配置UI组件
提供定时器配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class TimerConfigComponent(BaseComponent):
    """定时器配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建定时器配置界面
        
        Args:
            parent: 父组件
        """
        # 创建Notebook用于切换不同定时器
        notebook = ttk.Notebook(parent)
        notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        if self._is_chip_1521():
            # JZ8P1521: 只有 TCC 定时器
            info_label = ttk.Label(parent, 
                                  text="配置 TCC 定时器（8位定时计数器）",
                                  font=("Arial", 9), foreground="gray")
            info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
            
            tcc_frame = ttk.Frame(notebook, padding="10")
            notebook.add(tcc_frame, text="TCC")
            self._create_tcc_config_ui(tcc_frame)
        else:
            # JZ8P2615: 有 TC0/TC1/TC2 定时器
            info_label = ttk.Label(parent, 
                                  text="配置 TC0CON, TC0C, TC1, TC2等",
                                  font=("Arial", 9), foreground="gray")
            info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
            
            # TC0配置
            tc0_frame = ttk.Frame(notebook, padding="10")
            notebook.add(tc0_frame, text="TC0")
            self._create_tc0_config_ui(tc0_frame)
            
            # TC1配置
            tc1_frame = ttk.Frame(notebook, padding="10")
            notebook.add(tc1_frame, text="TC1")
            self._create_tc1_config_ui(tc1_frame)
            
            # TC2配置
            tc2_frame = ttk.Frame(notebook, padding="10")
            notebook.add(tc2_frame, text="TC2")
            self._create_tc2_config_ui(tc2_frame)
    
    def _create_tcc_config_ui(self, parent: tk.Widget):
        """创建TCC配置界面（JZ8P1521）"""
        config = self._get_config_safe("timer", "TCC", default={
            "enabled": False, "clock_source": "instruction", "prescaler": 0,
            "count_value": 0, "edge": "rising", "interrupt": False
        })
        
        # 使能
        enable_var = tk.BooleanVar(value=config.get("enabled", False))
        ttk.Checkbutton(parent, text="使能TCC", variable=enable_var,
                       command=lambda: self._update_timer_enabled("TCC", enable_var)).pack(anchor=tk.W, pady=5)
        
        # 时钟源
        ttk.Label(parent, text="时钟源:").pack(anchor=tk.W, pady=5)
        clk_var = tk.StringVar(value=config.get("clock_source", "instruction"))
        clk_combo = ttk.Combobox(parent, textvariable=clk_var,
                                values=["instruction", "system", "external"],
                                state="readonly", width=15)
        clk_combo.pack(anchor=tk.W, padx=20, pady=2)
        clk_combo.bind("<<ComboboxSelected>>",
                      lambda e: self._update_timer_config("TCC", "clock_source", clk_var.get()))
        
        # 边沿选择（仅外部时钟时有效）
        ttk.Label(parent, text="边沿选择（外部时钟）:").pack(anchor=tk.W, pady=5)
        edge_var = tk.StringVar(value=config.get("edge", "rising"))
        edge_combo = ttk.Combobox(parent, textvariable=edge_var,
                                 values=["rising", "falling"],
                                 state="readonly", width=15)
        edge_combo.pack(anchor=tk.W, padx=20, pady=2)
        edge_combo.bind("<<ComboboxSelected>>",
                       lambda e: self._update_timer_config("TCC", "edge", edge_var.get()))
        
        # 预分频
        ttk.Label(parent, text="预分频:").pack(anchor=tk.W, pady=5)
        prescaler_var = tk.IntVar(value=config.get("prescaler", 0))
        prescaler_spin = ttk.Spinbox(parent, from_=0, to=7, width=10, textvariable=prescaler_var)
        prescaler_spin.pack(anchor=tk.W, padx=20, pady=2)
        prescaler_var.trace_add("write",
                               lambda *args: self._update_timer_config("TCC", "prescaler", prescaler_var.get()))
        
        # 计数初值
        ttk.Label(parent, text="计数初值:").pack(anchor=tk.W, pady=5)
        count_var = tk.IntVar(value=config.get("count_value", 0))
        count_spin = ttk.Spinbox(parent, from_=0, to=255, width=10, textvariable=count_var)
        count_spin.pack(anchor=tk.W, padx=20, pady=2)
        count_var.trace_add("write",
                           lambda *args: self._update_timer_config("TCC", "count_value", count_var.get()))
        
        # 中断使能
        interrupt_var = tk.BooleanVar(value=config.get("interrupt", False))
        ttk.Checkbutton(parent, text="使能中断", variable=interrupt_var,
                       command=lambda: self._update_timer_config("TCC", "interrupt", interrupt_var.get())).pack(anchor=tk.W, pady=5)
    
    def _create_tc0_config_ui(self, parent: tk.Widget):
        """创建TC0配置界面"""
        config = self._get_config_safe("timer", "TC0", default={
            "enabled": False, "clock_source": "system", "prescaler": 0,
            "count_value": 206, "interrupt": False
        })
        
        # 使能
        enable_var = tk.BooleanVar(value=config["enabled"])
        ttk.Checkbutton(parent, text="使能TC0", variable=enable_var,
                       command=lambda: self._update_timer_enabled("TC0", enable_var)).pack(anchor=tk.W, pady=5)
        
        # 时钟源
        ttk.Label(parent, text="时钟源:").pack(anchor=tk.W, pady=5)
        clk_var = tk.StringVar(value=config["clock_source"])
        clk_combo = ttk.Combobox(parent, textvariable=clk_var,
                                values=["system", "instruction", "external"],
                                state="readonly", width=15)
        clk_combo.pack(anchor=tk.W, padx=20, pady=2)
        clk_combo.bind("<<ComboboxSelected>>",
                      lambda e: self._update_timer_clock_source("TC0", clk_var.get()))
        
        # 分频器
        ttk.Label(parent, text="分频器 (TCOPSR<2:0>):").pack(anchor=tk.W, pady=5)
        prescaler_var = tk.IntVar(value=config["prescaler"])
        prescaler_map = {0: "1:2", 1: "1:4", 2: "1:8", 3: "1:16", 
                         4: "1:32", 5: "1:64", 6: "1:128", 7: "1:256"}
        
        prescaler_frame = ttk.Frame(parent)
        prescaler_frame.pack(anchor=tk.W, padx=20, pady=2, fill=tk.X)
        prescaler_spin = ttk.Spinbox(prescaler_frame, from_=0, to=7, textvariable=prescaler_var,
                                    width=10, command=lambda: 
                                    self._update_timer_prescaler("TC0", prescaler_var.get()))
        prescaler_spin.pack(side=tk.LEFT)
        
        def update_prescaler_label(*args):
            val = prescaler_var.get()
            prescaler_label.config(text=f"分频系数: {prescaler_map[val]}")
        
        prescaler_var.trace('w', update_prescaler_label)
        prescaler_label = ttk.Label(prescaler_frame, text=f"分频系数: {prescaler_map[prescaler_var.get()]}")
        prescaler_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # 显示映射表
        map_text = "映射: 0=2分频, 1=4分频, 2=8分频, 3=16分频, 4=32分频, 5=64分频, 6=128分频, 7=256分频"
        ttk.Label(parent, text=map_text, font=("TkDefaultFont", 8), foreground="gray").pack(anchor=tk.W, padx=20, pady=2)
        
        # 计数值
        ttk.Label(parent, text="计数值:").pack(anchor=tk.W, pady=5)
        count_var = tk.IntVar(value=config["count_value"])
        count_spin = ttk.Spinbox(parent, from_=0, to=255, textvariable=count_var,
                                width=10, command=lambda:
                                self._update_timer_count("TC0", count_var.get()))
        count_spin.pack(anchor=tk.W, padx=20, pady=2)
        
        # 中断使能
        int_var = tk.BooleanVar(value=config["interrupt"])
        ttk.Checkbutton(parent, text="使能中断", variable=int_var,
                       command=lambda: self._update_timer_interrupt("TC0", int_var)).pack(anchor=tk.W, pady=5)
    
    def _create_tc1_config_ui(self, parent: tk.Widget):
        """创建TC1配置界面"""
        config = self._get_config_safe("timer", "TC1", default={
            "enabled": False, "mode": "10bit", "prescaler": 0,
            "period": 1000, "pwm_enabled": False, "interrupt": False
        })
        
        enable_var = tk.BooleanVar(value=config["enabled"])
        ttk.Checkbutton(parent, text="使能TC1", variable=enable_var,
                       command=lambda: self._update_timer_enabled("TC1", enable_var)).pack(anchor=tk.W, pady=5)
        
        ttk.Label(parent, text="模式:").pack(anchor=tk.W, pady=5)
        mode_var = tk.StringVar(value=config["mode"])
        mode_combo = ttk.Combobox(parent, textvariable=mode_var,
                                  values=["10bit", "20bit"],
                                  state="readonly", width=15)
        mode_combo.pack(anchor=tk.W, padx=20, pady=2)
        mode_combo.bind("<<ComboboxSelected>>",
                       lambda e: self._update_timer_mode("TC1", mode_var.get()))
        
        ttk.Label(parent, text="周期:").pack(anchor=tk.W, pady=5)
        period_var = tk.IntVar(value=config["period"])
        period_spin = ttk.Spinbox(parent, from_=0, to=65535, textvariable=period_var,
                                 width=10, command=lambda:
                                 self._update_timer_period("TC1", period_var.get()))
        period_spin.pack(anchor=tk.W, padx=20, pady=2)
        
        pwm_var = tk.BooleanVar(value=config["pwm_enabled"])
        ttk.Checkbutton(parent, text="关联PWM", variable=pwm_var,
                       command=lambda: self._update_timer_pwm("TC1", pwm_var)).pack(anchor=tk.W, pady=5)
        
        int_var = tk.BooleanVar(value=config["interrupt"])
        ttk.Checkbutton(parent, text="使能中断", variable=int_var,
                       command=lambda: self._update_timer_interrupt("TC1", int_var)).pack(anchor=tk.W, pady=5)
    
    def _create_tc2_config_ui(self, parent: tk.Widget):
        """创建TC2配置界面"""
        config = self._get_config_safe("timer", "TC2", default={
            "enabled": False, "mode": "10bit", "prescaler": 0,
            "period": 1000, "pwm_enabled": False, "interrupt": False
        })
        
        enable_var = tk.BooleanVar(value=config["enabled"])
        ttk.Checkbutton(parent, text="使能TC2", variable=enable_var,
                       command=lambda: self._update_timer_enabled("TC2", enable_var)).pack(anchor=tk.W, pady=5)
        
        ttk.Label(parent, text="模式:").pack(anchor=tk.W, pady=5)
        mode_var = tk.StringVar(value=config["mode"])
        mode_combo = ttk.Combobox(parent, textvariable=mode_var,
                                  values=["10bit", "20bit"],
                                  state="readonly", width=15)
        mode_combo.pack(anchor=tk.W, padx=20, pady=2)
        mode_combo.bind("<<ComboboxSelected>>",
                       lambda e: self._update_timer_mode("TC2", mode_var.get()))
        
        ttk.Label(parent, text="周期:").pack(anchor=tk.W, pady=5)
        period_var = tk.IntVar(value=config["period"])
        period_spin = ttk.Spinbox(parent, from_=0, to=65535, textvariable=period_var,
                                 width=10, command=lambda:
                                 self._update_timer_period("TC2", period_var.get()))
        period_spin.pack(anchor=tk.W, padx=20, pady=2)
        
        pwm_var = tk.BooleanVar(value=config["pwm_enabled"])
        ttk.Checkbutton(parent, text="关联PWM", variable=pwm_var,
                       command=lambda: self._update_timer_pwm("TC2", pwm_var)).pack(anchor=tk.W, pady=5)
        
        int_var = tk.BooleanVar(value=config["interrupt"])
        ttk.Checkbutton(parent, text="使能中断", variable=int_var,
                       command=lambda: self._update_timer_interrupt("TC2", int_var)).pack(anchor=tk.W, pady=5)
    
    def _update_timer_enabled(self, timer: str, var: tk.BooleanVar):
        """更新定时器使能"""
        if timer not in self.controller.config_data.get("timer", {}):
            if timer == "TCC":
                self.controller.config_data.setdefault("timer", {})[timer] = {
                    "enabled": False, "clock_source": "instruction", "prescaler": 0,
                    "count_value": 0, "edge": "rising", "interrupt": False
                }
        self.controller.config_data["timer"][timer]["enabled"] = var.get()
    
    def _update_timer_config(self, timer: str, key: str, value):
        """更新定时器配置（通用方法）"""
        if timer not in self.controller.config_data.get("timer", {}):
            if timer == "TCC":
                self.controller.config_data.setdefault("timer", {})[timer] = {
                    "enabled": False, "clock_source": "instruction", "prescaler": 0,
                    "count_value": 0, "edge": "rising", "interrupt": False
                }
        self.controller.config_data["timer"][timer][key] = value
    
    def _update_timer_clock_source(self, timer: str, value: str):
        """更新定时器时钟源"""
        self.controller.config_data["timer"][timer]["clock_source"] = value
    
    def _update_timer_prescaler(self, timer: str, value: int):
        """更新定时器分频器"""
        self.controller.config_data["timer"][timer]["prescaler"] = value
    
    def _update_timer_count(self, timer: str, value: int):
        """更新定时器计数值"""
        self.controller.config_data["timer"][timer]["count_value"] = value
    
    def _update_timer_mode(self, timer: str, value: str):
        """更新定时器模式"""
        self.controller.config_data["timer"][timer]["mode"] = value
    
    def _update_timer_period(self, timer: str, value: int):
        """更新定时器周期"""
        self.controller.config_data["timer"][timer]["period"] = value
    
    def _update_timer_pwm(self, timer: str, var: tk.BooleanVar):
        """更新定时器PWM关联"""
        self.controller.config_data["timer"][timer]["pwm_enabled"] = var.get()
    
    def _update_timer_interrupt(self, timer: str, var: tk.BooleanVar):
        """更新定时器中断使能"""
        self.controller.config_data["timer"][timer]["interrupt"] = var.get()

