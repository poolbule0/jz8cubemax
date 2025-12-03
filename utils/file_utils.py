#!/usr/bin/env python
# -*- coding: gbk -*-
"""
文件操作工具函数
提供文件读写等通用操作
"""


def read_file_with_encoding(filepath: str) -> str:
    """
    以多种编码方式尝试读取文件（GBK优先）
    
    Args:
        filepath: 文件路径
        
    Returns:
        文件内容字符串
        
    Raises:
        ValueError: 如果所有编码都失败
    """
    encodings = ['gbk', 'utf-8', 'gb2312', 'latin-1']
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            raise FileNotFoundError(f"文件不存在: {filepath}")
    raise ValueError(f"无法读取文件，所有编码都失败: {filepath}")

