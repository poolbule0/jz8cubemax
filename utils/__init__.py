#!/usr/bin/env python
# -*- coding: gbk -*-
"""
工具函数模块
提供通用的工具函数，包括寄存器计算、文件操作、配置验证等
"""

from .register_calc import (
    calculate_port_control,
    calculate_port_pull,
    compute_wdtcon_value,
    compute_inte0_value,
    compute_inte1_value
)
from .file_utils import read_file_with_encoding
from .config_validator import validate_config

__all__ = [
    'calculate_port_control',
    'calculate_port_pull',
    'compute_wdtcon_value',
    'compute_inte0_value',
    'compute_inte1_value',
    'read_file_with_encoding',
    'validate_config'
]

