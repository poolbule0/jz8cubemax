#!/usr/bin/env python
# -*- coding: gbk -*-
"""
Main配置UI组件
提供Main配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class MainConfigComponent(BaseComponent):
    """Main配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建Main配置界面
        
        Args:
            parent: 父组件
        """
        cfg_isr = self.controller.get_config().get("isr", {})
        
        title = ttk.Label(parent, text="main.c / main.h - 基础配置",
                         font=("Arial", 12, "bold"))
        title.pack(anchor=tk.W, pady=(5, 10))
        
        # 定时器计数常量配置
        if self._is_chip_1521():
            # JZ8P1521: 使用 TCC
            cfg_timer = self._get_config_safe("timer", "TCC", default={"count_value": 0, "enabled": False})
            timer_label = "TCC 计数常量 (TCC_NUM)"
        else:
            # JZ8P2615: 使用 TC0
            cfg_timer = self._get_config_safe("timer", "TC0", default={"count_value": 0, "enabled": False})
            timer_label = "TC0 计数常量 (TCC_NUM)"
        
        tcc_frame = ttk.LabelFrame(parent, text=timer_label, padding="10")
        tcc_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(tcc_frame, text="TCC_NUM:").grid(row=0, column=0, sticky=tk.W)
        tcc_var = tk.IntVar(value=cfg_timer.get("count_value", 0))
        spin = ttk.Spinbox(tcc_frame, from_=0, to=255, width=10, textvariable=tcc_var)
        spin.grid(row=0, column=1, sticky=tk.W, padx=5)
        tcc_var.trace_add("write",
                          lambda *args: self._update_timer_count("TC0", tcc_var.get()))
        
        ttk.Label(tcc_frame, text="说明: 对应 isr.c 中 TC0C += TCC_NUM 的增量").grid(
            row=1, column=0, columnspan=2, sticky=tk.W, pady=(4, 0))
        
        # 标志变量宏名（与 isr / main.h 联动）
        flag_frame = ttk.LabelFrame(parent, text="时间标志宏 (main.h)", padding="10")
        flag_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(flag_frame, text="10ms 标志宏名:").grid(row=0, column=0, sticky=tk.W, pady=2)
        t10_flag_var = tk.StringVar(value=cfg_isr.get("time_10ms_flag", "Time_10ms"))
        ttk.Entry(flag_frame, textvariable=t10_flag_var, width=20).grid(row=0, column=1, sticky=tk.W, pady=2)
        t10_flag_var.trace_add("write",
                               lambda *args: self._update_isr_config("time_10ms_flag", t10_flag_var.get()))
        
        ttk.Label(flag_frame, text="200us 标志宏名:").grid(row=1, column=0, sticky=tk.W, pady=2)
        t200_flag_var = tk.StringVar(value=cfg_isr.get("time_200us_flag", "Time_200us"))
        ttk.Entry(flag_frame, textvariable=t200_flag_var, width=20).grid(row=1, column=1, sticky=tk.W, pady=2)
        t200_flag_var.trace_add("write",
                                lambda *args: self._update_isr_config("time_200us_flag", t200_flag_var.get()))
        
        desc = ("main.h 中会生成对应的宏，例如:\n"
                "  #define {10ms宏名}   (U_Flage1.SYS_Flg.bit0)\n"
                "  #define {200us宏名}  (U_Flage1.SYS_Flg.bit1)")
        ttk.Label(flag_frame, text=desc, justify=tk.LEFT).grid(
            row=2, column=0, columnspan=2, sticky=tk.W, pady=(4, 0))
    
    def _update_timer_count(self, timer: str, value: int):
        """更新定时器计数值"""
        if timer == "TC0":
            if "timer" not in self.controller.config_data:
                self.controller.config_data["timer"] = {}
            if "TC0" not in self.controller.config_data["timer"]:
                self.controller.config_data["timer"]["TC0"] = {}
            self.controller.config_data["timer"]["TC0"]["count_value"] = value
        elif timer == "TCC":
            if "timer" not in self.controller.config_data:
                self.controller.config_data["timer"] = {}
            if "TCC" not in self.controller.config_data["timer"]:
                self.controller.config_data["timer"]["TCC"] = {}
            self.controller.config_data["timer"]["TCC"]["count_value"] = value
    
    def _update_isr_config(self, key: str, value):
        """更新ISR配置"""
        self.controller.config_data["isr"][key] = value

