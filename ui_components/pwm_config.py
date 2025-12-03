#!/usr/bin/env python
# -*- coding: gbk -*-
"""
PWM配置UI组件
提供PWM配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class PWMConfigComponent(BaseComponent):
    """PWM配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建PWM配置界面
        
        Args:
            parent: 父组件
        """
        info_label = ttk.Label(parent, 
                              text="配置 PWM相关寄存器",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        config = self.controller.get_config()["pwm"]
        
        # 创建表格
        table_frame = ttk.Frame(parent)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 表头
        headers = ["PWM通道", "使能", "周期(TCxPRD)", "占空比(%)", "输出引脚映射", "PWM时钟"]
        for i, header in enumerate(headers):
            ttk.Label(table_frame, text=header, font=("Arial", 10, "bold")).grid(
                row=0, column=i, padx=10, pady=5)
        
        # PWM通道配置
        clock_display_map = {"instruction": "指令周期", "system": "系统时钟"}
        reverse_clock_map = {v: k for k, v in clock_display_map.items()}
        
        # 根据芯片类型确定PWM列表
        if self._is_chip_1521():
            pwm_list = ["PWM1", "PWM2", "PWM3"]  # JZ8P1521 只有3路PWM
        else:
            pwm_list = ["PWM1", "PWM2", "PWM3", "PWM4"]  # JZ8P2615 有4路PWM
        
        for idx, pwm_name in enumerate(pwm_list, 1):
            row = idx
            pwm_config = config.get(pwm_name, {"enabled": False, "period": 100, "duty": 0, 
                                               "mapping": "P60", "clock_source": "instruction"})
            
            # 通道名
            ttk.Label(table_frame, text=pwm_name).grid(row=row, column=0, padx=10, pady=5)
            
            # 使能
            enable_var = tk.BooleanVar(value=pwm_config["enabled"])
            ttk.Checkbutton(table_frame, variable=enable_var,
                           command=lambda p=pwm_name, v=enable_var: 
                           self._update_pwm_enabled(p, v)).grid(row=row, column=1, padx=10, pady=5)

            # 周期
            period_var = tk.IntVar(value=pwm_config["period"])
            period_spin = ttk.Spinbox(
                table_frame,
                from_=0,
                to=1023,
                textvariable=period_var,
                width=10,
            )
            period_spin.grid(row=row, column=2, padx=10, pady=5)
            period_var.trace_add(
                "write",
                lambda *args, p=pwm_name, v=period_var: self._update_pwm_period(p, v.get()),
            )

            # 占空比
            duty_var = tk.IntVar(value=pwm_config["duty"])
            duty_spin = ttk.Spinbox(
                table_frame,
                from_=0,
                to=100,
                textvariable=duty_var,
                width=10,
            )
            duty_spin.grid(row=row, column=3, padx=10, pady=5)
            duty_var.trace_add(
                "write",
                lambda *args, p=pwm_name, v=duty_var: self._update_pwm_duty(p, v.get()),
            )

            # 引脚映射
            if pwm_name == "PWM1":
                options = ["P60", "P52"]
            elif pwm_name == "PWM2":
                options = ["P61", "P53"]
            elif pwm_name == "PWM3":
                options = ["P62", "P54"]
            else:  # PWM4
                options = ["P63", "P55"]

            mapping_var = tk.StringVar(value=pwm_config.get("mapping", options[0]))
            mapping_combo = ttk.Combobox(
                table_frame,
                textvariable=mapping_var,
                values=options,
                state="readonly",
                width=8,
            )
            mapping_combo.grid(row=row, column=4, padx=10, pady=5)
            mapping_combo.bind(
                "<<ComboboxSelected>>",
                lambda e, p=pwm_name, v=mapping_var: self._update_pwm_mapping(p, v.get()),
            )
            
            clock_key = pwm_config.get("clock_source", "instruction")
            clock_var = tk.StringVar(value=clock_display_map.get(clock_key, "指令周期"))
            clock_combo = ttk.Combobox(
                table_frame,
                textvariable=clock_var,
                values=list(clock_display_map.values()),
                state="readonly",
                width=10,
            )
            clock_combo.grid(row=row, column=5, padx=10, pady=5)
            clock_combo.bind(
                "<<ComboboxSelected>>",
                lambda e, p=pwm_name, cv=clock_var: self._update_pwm_clock_source(p, reverse_clock_map.get(cv.get(), "instruction")),
            )
    
    def _update_pwm_enabled(self, pwm: str, var: tk.BooleanVar):
        """更新PWM使能"""
        self.controller.config_data["pwm"][pwm]["enabled"] = var.get()
    
    def _update_pwm_period(self, pwm: str, value: int):
        """更新PWM周期"""
        self.controller.config_data["pwm"][pwm]["period"] = value
    
    def _update_pwm_duty(self, pwm: str, value: int):
        """更新PWM占空比"""
        self.controller.config_data["pwm"][pwm]["duty"] = value
    
    def _update_pwm_mapping(self, pwm: str, pin: str):
        """更新PWM输出引脚映射"""
        self.controller.config_data["pwm"][pwm]["mapping"] = pin
    
    def _update_pwm_clock_source(self, pwm: str, clock_key: str):
        """更新PWM时钟源"""
        self.controller.config_data["pwm"][pwm]["clock_source"] = clock_key

