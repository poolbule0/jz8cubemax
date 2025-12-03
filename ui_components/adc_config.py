#!/usr/bin/env python
# -*- coding: gbk -*-
"""
ADC配置UI组件
提供ADC配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class ADCConfigComponent(BaseComponent):
    """ADC配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建ADC配置界面
        
        Args:
            parent: 父组件
        """
        info_label = ttk.Label(parent, 
                              text="配置 P5ADE, P6ADE, ADCON0, ADCON1",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        # JZ8P1521 不支持 ADC，直接返回
        if self._is_chip_1521():
            no_adc_label = ttk.Label(parent, text="当前芯片不支持 ADC 功能", 
                                    foreground="gray", font=("Arial", 10))
            no_adc_label.pack(anchor=tk.W, padx=10, pady=20)
            return
        
        config = self._get_config_safe("adc", default={"enabled": False, "channels": [], 
                                                       "reference": "VDD", "clock_div": "Fosc/16", 
                                                       "calibration": False})
        
        # ADC使能
        adc_enable_var = tk.BooleanVar(value=config["enabled"])
        ttk.Checkbutton(parent, text="使能ADC", variable=adc_enable_var,
                       command=lambda: self._update_adc_enabled(adc_enable_var)).pack(anchor=tk.W, padx=10, pady=5)
        
        # 参考电压选择
        ttk.Label(parent, text="参考电压:").pack(anchor=tk.W, padx=10, pady=5)
        vref_var = tk.StringVar(value=config["reference"])
        vref_combo = ttk.Combobox(parent, textvariable=vref_var,
                                 values=["VDD", "4V", "3V", "2V", "1.5V"], 
                                 state="readonly", width=15)
        vref_combo.pack(anchor=tk.W, padx=30, pady=2)
        vref_combo.bind("<<ComboboxSelected>>", 
                       lambda e: self._update_adc_reference(vref_var.get()))
        
        # 时钟分频选择
        ttk.Label(parent, text="时钟分频:").pack(anchor=tk.W, padx=10, pady=5)
        clkdiv_var = tk.StringVar(value=config["clock_div"])
        clkdiv_combo = ttk.Combobox(parent, textvariable=clkdiv_var,
                                   values=["Fosc/1", "Fosc/4", "Fosc/16", "Fosc/64"],
                                   state="readonly", width=15)
        clkdiv_combo.pack(anchor=tk.W, padx=30, pady=2)
        clkdiv_combo.bind("<<ComboboxSelected>>",
                         lambda e: self._update_adc_clockdiv(clkdiv_var.get()))
        
        # 校准使能
        calib_var = tk.BooleanVar(value=config["calibration"])
        ttk.Checkbutton(parent, text="使能校准", variable=calib_var,
                       command=lambda: self._update_adc_calibration(calib_var)).pack(anchor=tk.W, padx=10, pady=5)
        
        # ADC通道选择
        ttk.Label(parent, text="ADC通道选择:").pack(anchor=tk.W, padx=10, pady=5)
        channel_frame = ttk.Frame(parent)
        channel_frame.pack(anchor=tk.W, padx=30, pady=2)
        
        channels = config.get("channels", [])
        channel_vars = {}
        for ch in range(14):
            var = tk.BooleanVar(value=ch in channels)
            channel_vars[ch] = var
            ch_name = f"AD{ch}"
            if ch < 6:
                ch_name += f" (P5{ch})"
            else:
                ch_name += f" (P6{ch-6})"
            ttk.Checkbutton(channel_frame, text=ch_name, variable=var,
                           command=lambda c=ch: self._update_adc_channels(channel_vars)).grid(
                           row=ch//7, column=ch%7, padx=5, pady=2, sticky=tk.W)
        
        # 存储控件引用
        if not hasattr(self, 'adc_widgets'):
            self.adc_widgets = {}
        self.adc_widgets['channels'] = channel_vars
        self.adc_widgets['enabled'] = adc_enable_var
        self.adc_widgets['reference'] = vref_var
        self.adc_widgets['clock_div'] = clkdiv_var
        self.adc_widgets['calibration'] = calib_var
    
    def _update_adc_enabled(self, var: tk.BooleanVar):
        """更新ADC使能状态"""
        self.controller.config_data["adc"]["enabled"] = var.get()
    
    def _update_adc_reference(self, value: str):
        """更新ADC参考电压"""
        self.controller.config_data["adc"]["reference"] = value
    
    def _update_adc_clockdiv(self, value: str):
        """更新ADC时钟分频"""
        self.controller.config_data["adc"]["clock_div"] = value
    
    def _update_adc_calibration(self, var: tk.BooleanVar):
        """更新ADC校准使能"""
        self.controller.config_data["adc"]["calibration"] = var.get()
    
    def _update_adc_channels(self, channel_vars: dict):
        """更新ADC通道选择"""
        channels = []
        for ch, var in channel_vars.items():
            if var.get():
                channels.append(ch)
        self.controller.config_data["adc"]["channels"] = channels

