#!/usr/bin/env python
# -*- coding: gbk -*-
"""
GPIO配置UI组件
提供GPIO端口配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class GPIOConfigComponent(BaseComponent):
    """GPIO配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建GPIO配置界面
        
        Args:
            parent: 父组件
        """
        # 创建Notebook用于切换P5和P6
        notebook = ttk.Notebook(parent)
        notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # P5端口配置
        p5_frame = ttk.Frame(notebook, padding="10")
        notebook.add(p5_frame, text="P5端口")
        self._create_port_config_ui(p5_frame, "P5")
        
        # P6端口配置
        p6_frame = ttk.Frame(notebook, padding="10")
        notebook.add(p6_frame, text="P6端口")
        self._create_port_config_ui(p6_frame, "P6", is_p6=True)
    
    def _create_port_config_ui(self, parent: tk.Widget, port_name: str, is_p6: bool = False):
        """创建端口配置界面"""
        config = self.controller.get_config()["gpio"][port_name]
        
        # 根据芯片类型和端口类型确定引脚数量
        if port_name == "P5":
            if self._is_chip_1521():
                pin_count = 4  # JZ8P1521 的 P5 只有 4 个引脚（P50-P53）
            else:
                pin_count = 8  # JZ8P2615 的 P5 有 8 个引脚
        else:
            pin_count = 8  # P6 有 8 个引脚
        
        # 创建表格框架
        table_frame = ttk.Frame(parent)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # 表头
        headers = ["引脚", "方向", "上拉", "下拉"]
        if is_p6:
            headers.extend(["开漏", "弱驱动"])
        # JZ8P1521 的 P5 不支持唤醒
        if not (port_name == "P5" and self._is_chip_1521()):
            headers.append("唤醒")
        
        for i, header in enumerate(headers):
            label = ttk.Label(table_frame, text=header, font=("Arial", 10, "bold"))
            label.grid(row=0, column=i, padx=5, pady=5, sticky=tk.W)
        
        # 存储控件引用
        if not hasattr(self, 'gpio_widgets'):
            self.gpio_widgets = {}
        if port_name not in self.gpio_widgets:
            self.gpio_widgets[port_name] = {}
        
        # 为每个引脚创建配置控件
        for pin in range(pin_count):
            row = pin + 1
            pin_name = f"{port_name}{pin}"
            
            # 引脚名称
            ttk.Label(table_frame, text=pin_name).grid(row=row, column=0, padx=5, pady=2)
            
            # 方向选择（输入/输出）- 安全访问，防止索引越界
            direction_list = config.get("direction", [0] * pin_count)
            if pin < len(direction_list):
                direction_value = direction_list[pin]
            else:
                direction_value = 0  # 默认输出
            direction_var = tk.StringVar(value="输出" if direction_value == 0 else "输入")
            direction_combo = ttk.Combobox(table_frame, textvariable=direction_var, 
                                          values=["输出", "输入"], state="readonly", width=8)
            direction_combo.grid(row=row, column=1, padx=5, pady=2)
            direction_combo.bind("<<ComboboxSelected>>", 
                               lambda e, p=pin, port=port_name: self._update_gpio_direction(p, port, e))
            self.gpio_widgets[port_name][f"direction_{pin}"] = direction_combo
            
            # 上拉使能 - 安全访问
            pullup_list = config.get("pullup", [1] * pin_count)
            if pin < len(pullup_list):
                pullup_value = pullup_list[pin]
            else:
                pullup_value = 1  # 默认禁止
            pullup_var = tk.BooleanVar(value=pullup_value == 0)
            pullup_check = ttk.Checkbutton(table_frame, variable=pullup_var,
                                          command=lambda p=pin, port=port_name: 
                                          self._update_gpio_pullup(p, port))
            pullup_check.grid(row=row, column=2, padx=5, pady=2)
            self.gpio_widgets[port_name][f"pullup_{pin}"] = pullup_var
            
            # 下拉使能 - 安全访问
            pulldown_list = config.get("pulldown", [1] * pin_count)
            if pin < len(pulldown_list):
                pulldown_value = pulldown_list[pin]
            else:
                pulldown_value = 1  # 默认禁止
            pulldown_var = tk.BooleanVar(value=pulldown_value == 0)
            pulldown_check = ttk.Checkbutton(table_frame, variable=pulldown_var,
                                           command=lambda p=pin, port=port_name: 
                                           self._update_gpio_pulldown(p, port))
            pulldown_check.grid(row=row, column=3, padx=5, pady=2)
            self.gpio_widgets[port_name][f"pulldown_{pin}"] = pulldown_var
            
            # P6特有：开漏和弱驱动
            if is_p6:
                # 开漏使能
                opendrain_var = tk.BooleanVar(value=config.get("opendrain", [0]*8)[pin] == 1)
                opendrain_check = ttk.Checkbutton(table_frame, variable=opendrain_var,
                                                 command=lambda p=pin, port=port_name: 
                                                 self._update_gpio_opendrain(p, port))
                opendrain_check.grid(row=row, column=4, padx=5, pady=2)
                self.gpio_widgets[port_name][f"opendrain_{pin}"] = opendrain_var
                
                # 弱驱动使能
                weakdrive_var = tk.BooleanVar(value=config.get("weakdrive", [0]*8)[pin] == 1)
                weakdrive_check = ttk.Checkbutton(table_frame, variable=weakdrive_var,
                                                 command=lambda p=pin, port=port_name: 
                                                 self._update_gpio_weakdrive(p, port))
                weakdrive_check.grid(row=row, column=5, padx=5, pady=2)
                self.gpio_widgets[port_name][f"weakdrive_{pin}"] = weakdrive_var
                
                # 唤醒使能（P6支持，P5在JZ8P1521不支持）
                if port_name == "P5" and self._is_chip_1521():
                    pass
                else:
                    wakeup_config = config.get("wakeup", [0] * 8)
                    if pin < len(wakeup_config):
                        wakeup_var = tk.BooleanVar(value=wakeup_config[pin] == 1)
                    else:
                        wakeup_var = tk.BooleanVar(value=False)
                    wakeup_check = ttk.Checkbutton(table_frame, variable=wakeup_var,
                                                 command=lambda p=pin, port=port_name: 
                                                 self._update_gpio_wakeup(p, port))
                    wakeup_check.grid(row=row, column=6, padx=5, pady=2)
                    self.gpio_widgets[port_name][f"wakeup_{pin}"] = wakeup_var
            else:
                # P5唤醒使能（JZ8P1521 的 P5 不支持唤醒）
                if port_name == "P5" and self._is_chip_1521():
                    pass
                else:
                    wakeup_config = config.get("wakeup", [0] * 8)
                    if pin < len(wakeup_config):
                        wakeup_var = tk.BooleanVar(value=wakeup_config[pin] == 1)
                    else:
                        wakeup_var = tk.BooleanVar(value=False)
                    wakeup_check = ttk.Checkbutton(table_frame, variable=wakeup_var,
                                                 command=lambda p=pin, port=port_name: 
                                                 self._update_gpio_wakeup(p, port))
                    wakeup_check.grid(row=row, column=4, padx=5, pady=2)
                    self.gpio_widgets[port_name][f"wakeup_{pin}"] = wakeup_var
    
    def _update_gpio_direction(self, pin: int, port: str, event):
        """更新GPIO方向配置"""
        widget = self.gpio_widgets[port][f"direction_{pin}"]
        value = 1 if widget.get() == "输入" else 0
        self.controller.config_data["gpio"][port]["direction"][pin] = value
    
    def _update_gpio_pullup(self, pin: int, port: str):
        """更新GPIO上拉配置"""
        var = self.gpio_widgets[port][f"pullup_{pin}"]
        value = 0 if var.get() else 1  # 0=使能, 1=禁止
        self.controller.config_data["gpio"][port]["pullup"][pin] = value
    
    def _update_gpio_pulldown(self, pin: int, port: str):
        """更新GPIO下拉配置"""
        var = self.gpio_widgets[port][f"pulldown_{pin}"]
        value = 0 if var.get() else 1  # 0=使能, 1=禁止
        self.controller.config_data["gpio"][port]["pulldown"][pin] = value
    
    def _update_gpio_opendrain(self, pin: int, port: str):
        """更新GPIO开漏配置"""
        var = self.gpio_widgets[port][f"opendrain_{pin}"]
        value = 1 if var.get() else 0  # 0=禁止, 1=使能
        self.controller.config_data["gpio"][port]["opendrain"][pin] = value
    
    def _update_gpio_weakdrive(self, pin: int, port: str):
        """更新GPIO弱驱动配置"""
        var = self.gpio_widgets[port][f"weakdrive_{pin}"]
        value = 1 if var.get() else 0  # 0=禁止, 1=使能
        self.controller.config_data["gpio"][port]["weakdrive"][pin] = value
    
    def _update_gpio_wakeup(self, pin: int, port: str):
        """更新GPIO唤醒配置"""
        var = self.gpio_widgets[port][f"wakeup_{pin}"]
        value = 1 if var.get() else 0  # 0=禁止, 1=使能
        self.controller.config_data["gpio"][port]["wakeup"][pin] = value

