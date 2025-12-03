#!/usr/bin/env python
# -*- coding: gbk -*-
"""
芯片支持模块
提供多芯片代码生成的抽象接口
"""

from .chip_base import ChipBase
from .jz8p2615 import JZ8P2615Chip
from .jz8p1521 import JZ8P1521
from .chip_registry import ChipRegistry

__all__ = ['ChipBase', 'JZ8P2615Chip', 'JZ8P1521', 'ChipRegistry']

