#!/usr/bin/env python
# -*- coding: gbk -*-
"""
中断配置UI组件
提供中断配置界面
"""

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING
from .base_component import BaseComponent

if TYPE_CHECKING:
    from control import ConfigController


class InterruptConfigComponent(BaseComponent):
    """中断配置组件"""
    
    def create_config_ui(self, parent: tk.Widget):
        """
        创建中断寄存器配置界面
        
        Args:
            parent: 父组件
        """
        config = self.controller.get_config()["interrupt"]
        
        # 根据芯片类型显示不同的配置界面
        if self._is_chip_1521():
            self._create_1521_interrupt_ui(parent, config)
        else:
            self._create_2615_interrupt_ui(parent, config)
    
    def _create_1521_interrupt_ui(self, parent: tk.Widget, config: dict):
        """创建JZ8P1521的中断配置界面"""
        info_label = ttk.Label(parent, 
                              text="配置 IOCE(WDTCR) 和 IOCF(IMR) 中断寄存器",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        # IOCE (WDTCR) 寄存器配置
        ioce_frame = ttk.LabelFrame(parent, text="IOCE (WDTCR) - WDT控制及外部中断使能", padding="10")
        ioce_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # WDT使能 (Bit7)
        system_config = self.controller.get_config().get("system", {})
        wdt_config = system_config.get("wdt", {})
        wdt_enabled = wdt_config.get("enabled", False)
        wdt_enable_var = tk.BooleanVar(value=wdt_enabled)
        ttk.Checkbutton(ioce_frame, text="WDT使能 (Bit7)", variable=wdt_enable_var,
                       command=lambda: self._update_1521_wdt_enable(wdt_enable_var)).pack(anchor=tk.W, pady=2)
        
        # 外部中断使能 (Bit6: EIS)
        exint_config = config.get("EXINT", {})
        eis_enabled = exint_config.get("enabled", False)
        eis_enable_var = tk.BooleanVar(value=eis_enabled)
        ttk.Checkbutton(ioce_frame, text="外部中断使能 EIS (P60, Bit6)", variable=eis_enable_var,
                       command=lambda: self._update_1521_eis_enable(eis_enable_var)).pack(anchor=tk.W, pady=2)
        
        # IOCF (IMR) 寄存器配置
        iocf_frame = ttk.LabelFrame(parent, text="IOCF (IMR) - 中断使能控制寄存器", padding="10")
        iocf_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # T1IE (Bit3)
        t1_pwm_config = config.get("T1_PWM", {})
        t1ie_enabled = t1_pwm_config.get("enabled", False)
        t1ie_var = tk.BooleanVar(value=t1ie_enabled)
        ttk.Checkbutton(iocf_frame, text="T1/PWM周期中断使能 T1IE (Bit3)", variable=t1ie_var,
                       command=lambda: self._update_1521_t1ie(t1ie_var)).pack(anchor=tk.W, pady=2)
        
        # EXIE (Bit2)
        exie_var = tk.BooleanVar(value=eis_enabled)
        ttk.Checkbutton(iocf_frame, text="外部中断使能 EXIE (Bit2)", variable=exie_var,
                       command=lambda: self._update_1521_exie(exie_var)).pack(anchor=tk.W, pady=2)
        
        # ICIE (Bit1)
        port_change_config = config.get("PORT_CHANGE", {})
        icie_enabled = port_change_config.get("enabled", False)
        icie_var = tk.BooleanVar(value=icie_enabled)
        ttk.Checkbutton(iocf_frame, text="P6端口状态改变中断使能 ICIE (Bit1)", variable=icie_var,
                       command=lambda: self._update_1521_icie(icie_var)).pack(anchor=tk.W, pady=2)
        
        # TCIE (Bit0)
        tcc_config = config.get("TCC", {})
        tcie_enabled = tcc_config.get("enabled", False)
        tcie_var = tk.BooleanVar(value=tcie_enabled)
        ttk.Checkbutton(iocf_frame, text="TCC溢出中断使能 TCIE (Bit0)", variable=tcie_var,
                       command=lambda: self._update_1521_tcie(tcie_var)).pack(anchor=tk.W, pady=2)
    
    def _create_2615_interrupt_ui(self, parent: tk.Widget, config: dict):
        """创建JZ8P2615的中断配置界面"""
        info_label = ttk.Label(parent, 
                              text="配置 WDTCON, INTE0, INTE1, INTF0, INTF1",
                              font=("Arial", 9), foreground="gray")
        info_label.pack(anchor=tk.W, padx=10, pady=(5, 10))
        
        # WDTCON寄存器配置
        wdtcon_frame = ttk.LabelFrame(parent, text="WDTCON - 外部中断控制寄存器", padding="10")
        wdtcon_frame.pack(fill=tk.X, padx=10, pady=5)
        
        wdtcon_config = config.get("wdtcon", {})
        
        # WDT使能
        wdt_enable_var = tk.BooleanVar(value=wdtcon_config["wdt_enabled"])
        ttk.Checkbutton(wdtcon_frame, text="WDT使能 (Bit7)", variable=wdt_enable_var,
                       command=lambda: self._update_wdtcon_wdt(wdt_enable_var)).pack(anchor=tk.W, pady=2)
        
        # INT0配置
        int0_frame = ttk.Frame(wdtcon_frame)
        int0_frame.pack(fill=tk.X, pady=2)
        int0_enable_var = tk.BooleanVar(value=wdtcon_config["int0_enabled"])
        ttk.Checkbutton(int0_frame, text="INT0使能 (P60, Bit6)", variable=int0_enable_var,
                       command=lambda: self._update_wdtcon_int0_enable(int0_enable_var)).pack(side=tk.LEFT, padx=5)
        int0_edge_var = tk.StringVar(value=wdtcon_config["int0_edge"])
        ttk.Label(int0_frame, text="触发边沿:").pack(side=tk.LEFT, padx=5)
        ttk.Combobox(int0_frame, textvariable=int0_edge_var, values=["rising", "falling"],
                    state="readonly", width=10).pack(side=tk.LEFT, padx=5)
        int0_edge_var.trace("w", lambda *args: self._update_wdtcon_int0_edge(int0_edge_var.get()))
        
        # INT1配置
        int1_frame = ttk.Frame(wdtcon_frame)
        int1_frame.pack(fill=tk.X, pady=2)
        int1_enable_var = tk.BooleanVar(value=wdtcon_config["int1_enabled"])
        ttk.Checkbutton(int1_frame, text="INT1使能 (P53, Bit5)", variable=int1_enable_var,
                       command=lambda: self._update_wdtcon_int1_enable(int1_enable_var)).pack(side=tk.LEFT, padx=5)
        int1_edge_var = tk.StringVar(value=wdtcon_config["int1_edge"])
        ttk.Label(int1_frame, text="触发边沿:").pack(side=tk.LEFT, padx=5)
        ttk.Combobox(int1_frame, textvariable=int1_edge_var, values=["rising", "falling"],
                    state="readonly", width=10).pack(side=tk.LEFT, padx=5)
        int1_edge_var.trace("w", lambda *args: self._update_wdtcon_int1_edge(int1_edge_var.get()))
        
        # 内部基准输出
        vfoe_var = tk.BooleanVar(value=wdtcon_config["vfoe"])
        ttk.Checkbutton(wdtcon_frame, text="内部基准输出使能 (Bit4)", variable=vfoe_var,
                       command=lambda: self._update_wdtcon_vfoe(vfoe_var)).pack(anchor=tk.W, pady=2)
        
        # INTE0寄存器配置
        inte0_frame = ttk.LabelFrame(parent, text="INTE0 - 中断使能控制寄存器0", padding="10")
        inte0_frame.pack(fill=tk.X, padx=10, pady=5)
        
        inte0_config = config["inte0"]
        
        ad_ie_var = tk.BooleanVar(value=inte0_config["ad_ie"])
        ttk.Checkbutton(inte0_frame, text="ADC中断使能 (Bit5)", variable=ad_ie_var,
                       command=lambda: self._update_inte0_ad_ie(ad_ie_var)).pack(anchor=tk.W, pady=2)
        
        ex1_ie_var = tk.BooleanVar(value=inte0_config["ex1_ie"])
        ttk.Checkbutton(inte0_frame, text="INT1中断使能 (Bit4)", variable=ex1_ie_var,
                       command=lambda: self._update_inte0_ex1_ie(ex1_ie_var)).pack(anchor=tk.W, pady=2)
        
        ex0_ie_var = tk.BooleanVar(value=inte0_config["ex0_ie"])
        ttk.Checkbutton(inte0_frame, text="INT0中断使能 (Bit3)", variable=ex0_ie_var,
                       command=lambda: self._update_inte0_ex0_ie(ex0_ie_var)).pack(anchor=tk.W, pady=2)
        
        p6ic_ie_var = tk.BooleanVar(value=inte0_config["p6ic_ie"])
        ttk.Checkbutton(inte0_frame, text="P6端口变化中断使能 (Bit2)", variable=p6ic_ie_var,
                       command=lambda: self._update_inte0_p6ic_ie(p6ic_ie_var)).pack(anchor=tk.W, pady=2)
        
        p5ic_ie_var = tk.BooleanVar(value=inte0_config["p5ic_ie"])
        ttk.Checkbutton(inte0_frame, text="P5端口变化中断使能 (Bit1)", variable=p5ic_ie_var,
                       command=lambda: self._update_inte0_p5ic_ie(p5ic_ie_var)).pack(anchor=tk.W, pady=2)
        
        tc0_ie_var = tk.BooleanVar(value=inte0_config["tc0_ie"])
        ttk.Checkbutton(inte0_frame, text="TC0中断使能 (Bit0)", variable=tc0_ie_var,
                       command=lambda: self._update_inte0_tc0_ie(tc0_ie_var)).pack(anchor=tk.W, pady=2)
        
        # INTE1寄存器配置
        inte1_frame = ttk.LabelFrame(parent, text="INTE1 - 中断使能控制寄存器1", padding="10")
        inte1_frame.pack(fill=tk.X, padx=10, pady=5)
        
        inte1_config = config["inte1"]
        
        dt4_ie_var = tk.BooleanVar(value=inte1_config["dt4_ie"])
        ttk.Checkbutton(inte1_frame, text="DT4中断使能 (Bit5)", variable=dt4_ie_var,
                       command=lambda: self._update_inte1_dt4_ie(dt4_ie_var)).pack(anchor=tk.W, pady=2)
        
        dt3_ie_var = tk.BooleanVar(value=inte1_config["dt3_ie"])
        ttk.Checkbutton(inte1_frame, text="DT3中断使能 (Bit4)", variable=dt3_ie_var,
                       command=lambda: self._update_inte1_dt3_ie(dt3_ie_var)).pack(anchor=tk.W, pady=2)
        
        dt2_ie_var = tk.BooleanVar(value=inte1_config["dt2_ie"])
        ttk.Checkbutton(inte1_frame, text="DT2中断使能 (Bit3)", variable=dt2_ie_var,
                       command=lambda: self._update_inte1_dt2_ie(dt2_ie_var)).pack(anchor=tk.W, pady=2)
        
        dt1_ie_var = tk.BooleanVar(value=inte1_config["dt1_ie"])
        ttk.Checkbutton(inte1_frame, text="DT1中断使能 (Bit2)", variable=dt1_ie_var,
                       command=lambda: self._update_inte1_dt1_ie(dt1_ie_var)).pack(anchor=tk.W, pady=2)
        
        tc2_ie_var = tk.BooleanVar(value=inte1_config["tc2_ie"])
        ttk.Checkbutton(inte1_frame, text="TC2中断使能 (Bit1)", variable=tc2_ie_var,
                       command=lambda: self._update_inte1_tc2_ie(tc2_ie_var)).pack(anchor=tk.W, pady=2)
        
        tc1_ie_var = tk.BooleanVar(value=inte1_config["tc1_ie"])
        ttk.Checkbutton(inte1_frame, text="TC1中断使能 (Bit0)", variable=tc1_ie_var,
                       command=lambda: self._update_inte1_tc1_ie(tc1_ie_var)).pack(anchor=tk.W, pady=2)
    
    def _update_wdtcon_wdt(self, var: tk.BooleanVar):
        """更新WDTCON WDT使能"""
        self.controller.config_data["interrupt"]["wdtcon"]["wdt_enabled"] = var.get()
    
    def _update_wdtcon_int0_enable(self, var: tk.BooleanVar):
        """更新WDTCON INT0使能"""
        self.controller.config_data["interrupt"]["wdtcon"]["int0_enabled"] = var.get()
    
    def _update_wdtcon_int0_edge(self, value: str):
        """更新WDTCON INT0触发边沿"""
        self.controller.config_data["interrupt"]["wdtcon"]["int0_edge"] = value
    
    def _update_wdtcon_int1_enable(self, var: tk.BooleanVar):
        """更新WDTCON INT1使能"""
        self.controller.config_data["interrupt"]["wdtcon"]["int1_enabled"] = var.get()
    
    def _update_wdtcon_int1_edge(self, value: str):
        """更新WDTCON INT1触发边沿"""
        self.controller.config_data["interrupt"]["wdtcon"]["int1_edge"] = value
    
    def _update_wdtcon_vfoe(self, var: tk.BooleanVar):
        """更新WDTCON 内部基准输出使能"""
        self.controller.config_data["interrupt"]["wdtcon"]["vfoe"] = var.get()
    
    def _update_inte0_ad_ie(self, var: tk.BooleanVar):
        """更新INTE0 ADC中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["ad_ie"] = var.get()
    
    def _update_inte0_ex1_ie(self, var: tk.BooleanVar):
        """更新INTE0 INT1中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["ex1_ie"] = var.get()
    
    def _update_inte0_ex0_ie(self, var: tk.BooleanVar):
        """更新INTE0 INT0中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["ex0_ie"] = var.get()
    
    def _update_inte0_p6ic_ie(self, var: tk.BooleanVar):
        """更新INTE0 P6端口变化中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["p6ic_ie"] = var.get()
    
    def _update_inte0_p5ic_ie(self, var: tk.BooleanVar):
        """更新INTE0 P5端口变化中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["p5ic_ie"] = var.get()
    
    def _update_inte0_tc0_ie(self, var: tk.BooleanVar):
        """更新INTE0 TC0中断使能"""
        self.controller.config_data["interrupt"]["inte0"]["tc0_ie"] = var.get()
    
    def _update_inte1_dt4_ie(self, var: tk.BooleanVar):
        """更新INTE1 DT4中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["dt4_ie"] = var.get()
    
    def _update_inte1_dt3_ie(self, var: tk.BooleanVar):
        """更新INTE1 DT3中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["dt3_ie"] = var.get()
    
    def _update_inte1_dt2_ie(self, var: tk.BooleanVar):
        """更新INTE1 DT2中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["dt2_ie"] = var.get()
    
    def _update_inte1_dt1_ie(self, var: tk.BooleanVar):
        """更新INTE1 DT1中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["dt1_ie"] = var.get()
    
    def _update_inte1_tc2_ie(self, var: tk.BooleanVar):
        """更新INTE1 TC2中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["tc2_ie"] = var.get()
    
    def _update_inte1_tc1_ie(self, var: tk.BooleanVar):
        """更新INTE1 TC1中断使能"""
        self.controller.config_data["interrupt"]["inte1"]["tc1_ie"] = var.get()
    
    # JZ8P1521 专用更新方法
    def _update_1521_wdt_enable(self, var: tk.BooleanVar):
        """更新JZ8P1521 WDT使能"""
        if "system" not in self.controller.config_data:
            self.controller.config_data["system"] = {}
        if "wdt" not in self.controller.config_data["system"]:
            self.controller.config_data["system"]["wdt"] = {}
        self.controller.config_data["system"]["wdt"]["enabled"] = var.get()
    
    def _update_1521_eis_enable(self, var: tk.BooleanVar):
        """更新JZ8P1521 外部中断使能 (EIS)"""
        if "EXINT" not in self.controller.config_data["interrupt"]:
            self.controller.config_data["interrupt"]["EXINT"] = {}
        self.controller.config_data["interrupt"]["EXINT"]["enabled"] = var.get()
    
    def _update_1521_t1ie(self, var: tk.BooleanVar):
        """更新JZ8P1521 T1IE中断使能"""
        if "T1_PWM" not in self.controller.config_data["interrupt"]:
            self.controller.config_data["interrupt"]["T1_PWM"] = {}
        self.controller.config_data["interrupt"]["T1_PWM"]["enabled"] = var.get()
    
    def _update_1521_exie(self, var: tk.BooleanVar):
        """更新JZ8P1521 EXIE中断使能"""
        if "EXINT" not in self.controller.config_data["interrupt"]:
            self.controller.config_data["interrupt"]["EXINT"] = {}
        self.controller.config_data["interrupt"]["EXINT"]["enabled"] = var.get()
    
    def _update_1521_icie(self, var: tk.BooleanVar):
        """更新JZ8P1521 ICIE中断使能"""
        if "PORT_CHANGE" not in self.controller.config_data["interrupt"]:
            self.controller.config_data["interrupt"]["PORT_CHANGE"] = {}
        self.controller.config_data["interrupt"]["PORT_CHANGE"]["enabled"] = var.get()
    
    def _update_1521_tcie(self, var: tk.BooleanVar):
        """更新JZ8P1521 TCIE中断使能"""
        if "TCC" not in self.controller.config_data["interrupt"]:
            self.controller.config_data["interrupt"]["TCC"] = {}
        self.controller.config_data["interrupt"]["TCC"]["enabled"] = var.get()

