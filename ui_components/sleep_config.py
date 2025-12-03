#!/usr/bin/env python
# -*- coding: gbk -*-
"""
睡眠配置UI组件
提供睡眠配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class SleepConfigComponent(BaseComponent):
    """睡眠配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建睡眠配置界面
        
        Args:
            parent: 父组件
        """
        # 根据芯片类型使用不同的默认配置
        if self._is_chip_1521():
            default_sleep = {
                "enabled": False,
                "mode": "sleep",
                "wakeup": {"wdt": False, "port_change": False, "tcc": False, "pwm": False},
                "wake_ports": []
            }
        else:
            default_sleep = {
                "enabled": False, "counter_name": "sleep_cnt", "threshold": 5,
                "condition": "F_CHARGE == 0 && F_CHARGE_FULL == 0 && r_g_workMod == 0",
                "wake_ports": ["P6"]
            }
        
        cfg = self._get_config_safe("sleep", default=default_sleep)
        
        ttk.Label(parent, text="sleep.c - 睡眠配置",
                  font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(5, 10))
        
        enable_var = tk.BooleanVar(value=cfg.get("enabled", False))
        ttk.Checkbutton(parent, text="启用睡眠功能", variable=enable_var,
                       command=lambda: self._update_sleep_config("enabled", enable_var.get())
                       ).pack(anchor=tk.W, padx=5, pady=5)
        
        # JZ8P1521 的 sleep 配置结构不同，需要特殊处理
        if self._is_chip_1521():
            # JZ8P1521 的 sleep 配置可能没有 counter_name 等字段
            # 显示简化的配置界面
            block = ttk.LabelFrame(parent, text="睡眠参数", padding="10")
            block.pack(fill=tk.X, padx=5, pady=5)
            
            # 睡眠模式选择
            ttk.Label(block, text="睡眠模式:").grid(row=0, column=0, sticky=tk.W, pady=2)
            mode_var = tk.StringVar(value=cfg.get("mode", "sleep"))
            mode_combo = ttk.Combobox(block, textvariable=mode_var,
                                     values=["sleep", "idle"],
                                     state="readonly", width=15)
            mode_combo.grid(row=0, column=1, sticky=tk.W, pady=2)
            mode_combo.bind("<<ComboboxSelected>>",
                           lambda e: self._update_sleep_config("mode", mode_var.get()))
        else:
            # JZ8P2615 的 sleep 配置
            block = ttk.LabelFrame(parent, text="睡眠参数", padding="10")
            block.pack(fill=tk.X, padx=5, pady=5)
            
            ttk.Label(block, text="计数变量名:").grid(row=0, column=0, sticky=tk.W, pady=2)
            counter_var = tk.StringVar(value=cfg.get("counter_name", "sleep_cnt"))
            ttk.Entry(block, textvariable=counter_var, width=20).grid(row=0, column=1, sticky=tk.W, pady=2)
            counter_var.trace_add("write",
                                  lambda *args: self._update_sleep_config("counter_name", counter_var.get()))
            
            ttk.Label(block, text="阈值:").grid(row=1, column=0, sticky=tk.W, pady=2)
            threshold_var = tk.IntVar(value=cfg.get("threshold", 5))
            ttk.Spinbox(block, from_=1, to=255, width=10,
                        textvariable=threshold_var).grid(row=1, column=1, sticky=tk.W, pady=2)
            threshold_var.trace_add("write",
                                    lambda *args: self._update_sleep_config("threshold", threshold_var.get()))
            
            ttk.Label(block, text="进入睡眠条件表达式:").grid(row=2, column=0, sticky=tk.W, pady=2)
            condition_var = tk.StringVar(value=cfg.get("condition", ""))
            ttk.Entry(block, textvariable=condition_var, width=50).grid(row=2, column=1, sticky=tk.W, pady=2)
            condition_var.trace_add("write",
                                    lambda *args: self._update_sleep_config("condition", condition_var.get()))
        
        # 唤醒端口配置（两种芯片都支持）
        wake_frame = ttk.LabelFrame(parent, text="唤醒端口", padding="10")
        wake_frame.pack(fill=tk.X, padx=5, pady=5)
        wake_ports = cfg.get("wake_ports", ["P6"])
        
        # JZ8P1521 的 P5 不支持唤醒
        if not self._is_chip_1521():
            p5_var = tk.BooleanVar(value="P5" in wake_ports)
            ttk.Checkbutton(wake_frame, text="P5 端口唤醒", variable=p5_var,
                            command=lambda: self._update_sleep_wake_port("P5", p5_var.get())
                            ).grid(row=0, column=0, sticky=tk.W, pady=2)
        
        p6_var = tk.BooleanVar(value="P6" in wake_ports)
        ttk.Checkbutton(wake_frame, text="P6 端口唤醒", variable=p6_var,
                        command=lambda: self._update_sleep_wake_port("P6", p6_var.get())
                        ).grid(row=0, column=1 if self._is_chip_1521() else 1, sticky=tk.W, pady=2)
    
    def _update_sleep_config(self, key: str, value):
        """更新睡眠配置"""
        if "sleep" not in self.controller.config_data:
            self.controller.config_data["sleep"] = {}
        self.controller.config_data["sleep"][key] = value
    
    def _update_sleep_wake_port(self, port: str, enabled: bool):
        """更新睡眠唤醒端口"""
        if "sleep" not in self.controller.config_data:
            self.controller.config_data["sleep"] = {}
        if "wake_ports" not in self.controller.config_data["sleep"]:
            self.controller.config_data["sleep"]["wake_ports"] = []
        
        wake_ports = self.controller.config_data["sleep"]["wake_ports"]
        if enabled and port not in wake_ports:
            wake_ports.append(port)
        elif not enabled and port in wake_ports:
            wake_ports.remove(port)

