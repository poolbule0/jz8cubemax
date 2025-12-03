#!/usr/bin/env python
# -*- coding: gbk -*-
"""
寄存器计算工具函数
提供各种寄存器值的计算功能
"""

from typing import List


def calculate_port_control(direction_list: List[int]) -> int:
    """
    计算端口控制寄存器值
    
    Args:
        direction_list: 方向列表，0=输出, 1=输入
        
    Returns:
        寄存器值
    """
    value = 0
    for i, dir_val in enumerate(direction_list):
        if dir_val == 1:  # 输入
            value |= (1 << i)
    return value


def calculate_port_pull(pull_list: List[int], invert: bool = False) -> int:
    """
    计算上拉/下拉寄存器值
    
    Args:
        pull_list: 上拉/下拉配置列表
        invert: 是否反转逻辑（对于开漏、弱驱动、唤醒等）
        
    Returns:
        寄存器值
    """
    value = 0
    for i, pull_val in enumerate(pull_list):
        if invert:
            # 对于开漏、弱驱动、唤醒：0=禁止，1=使能
            if pull_val == 1:  # 使能
                value |= (1 << i)
        else:
            # 对于上拉/下拉：0=使能，1=禁止
            # 寄存器位：0=使能，1=禁止
            # 所以如果配置是1（禁止），寄存器位应该是1
            if pull_val == 1:  # 禁止，寄存器位设为1
                value |= (1 << i)
            # 如果配置是0（使能），寄存器位应该是0，不需要设置
    return value


def compute_wdtcon_value(int_config: dict) -> int:
    """
    计算WDTCON寄存器值
    
    Args:
        int_config: 中断配置字典
        
    Returns:
        WDTCON寄存器值
    """
    wdtcon = 0x00
    wdtcon_config = int_config["wdtcon"]
    if wdtcon_config["wdt_enabled"]:
        wdtcon |= 0x80  # Bit7: WDT使能
    if wdtcon_config["int0_enabled"]:
        wdtcon |= 0x40  # Bit6: P60外部中断使能
    if wdtcon_config["int1_enabled"]:
        wdtcon |= 0x20  # Bit5: P53外部中断使能
    if wdtcon_config["vfoe"]:
        wdtcon |= 0x10  # Bit4: 内部基准输出使能
    if wdtcon_config["int1_edge"] == "rising":
        wdtcon |= 0x08  # Bit3: INT1上升沿触发
    if wdtcon_config["int0_edge"] == "rising":
        wdtcon |= 0x04  # Bit2: INT0上升沿触发
    return wdtcon


def compute_inte0_value(int_config: dict) -> int:
    """
    计算INTE0寄存器值
    
    Args:
        int_config: 中断配置字典
        
    Returns:
        INTE0寄存器值
    """
    inte0 = 0x00
    inte0_config = int_config["inte0"]
    if inte0_config["ad_ie"]:
        inte0 |= 0x20
    if inte0_config["ex1_ie"]:
        inte0 |= 0x10
    if inte0_config["ex0_ie"]:
        inte0 |= 0x08
    if inte0_config["p6ic_ie"]:
        inte0 |= 0x04
    if inte0_config["p5ic_ie"]:
        inte0 |= 0x02
    if inte0_config["tc0_ie"]:
        inte0 |= 0x01
    return inte0


def compute_inte1_value(int_config: dict) -> int:
    """
    计算INTE1寄存器值
    
    Args:
        int_config: 中断配置字典
        
    Returns:
        INTE1寄存器值
    """
    inte1 = 0x00
    inte1_config = int_config["inte1"]
    if inte1_config["dt4_ie"]:
        inte1 |= 0x20
    if inte1_config["dt3_ie"]:
        inte1 |= 0x10
    if inte1_config["dt2_ie"]:
        inte1 |= 0x08
    if inte1_config["dt1_ie"]:
        inte1 |= 0x04
    if inte1_config["tc2_ie"]:
        inte1 |= 0x02
    if inte1_config["tc1_ie"]:
        inte1 |= 0x01
    return inte1

