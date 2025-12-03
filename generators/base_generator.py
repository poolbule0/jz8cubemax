#!/usr/bin/env python
# -*- coding: gbk -*-
"""
代码生成基类
定义所有代码生成器的通用接口和基础功能
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional


class BaseGenerator(ABC):
    """代码生成器基类"""
    
    def __init__(self, config_data: Dict[str, Any], chip_name: str, header_file_name: str):
        """
        初始化生成器
        
        Args:
            config_data: 配置数据字典
            chip_name: 芯片名称
            header_file_name: 芯片头文件名
        """
        self.config_data = config_data
        self.chip_name = chip_name
        self.header_file_name = header_file_name
    
    def _should_include_comments(self) -> bool:
        """检查是否应该包含注释"""
        return self.config_data.get("code_generation", {}).get("include_comments", True)
    
    def _add_comment(self, code_list: List[str], comment: str, inline: bool = False) -> None:
        """
        根据配置决定是否添加注释
        
        Args:
            code_list: 代码列表
            comment: 注释内容（不包含 // 或 /* */）
            inline: 是否为行内注释（True）或独立注释行（False）
        """
        if not self._should_include_comments():
            return
        
        if inline:
            # 行内注释：在现有代码行后添加
            code_list.append(f"// {comment}")
        else:
            # 独立注释行
            if comment.startswith("//") or comment.startswith("/*"):
                # 如果已经包含注释标记，直接添加
                code_list.append(comment)
            else:
                code_list.append(f"// {comment}")
    
    def _add_code_with_comment(self, code_list: List[str], code_line: str, comment: str = "") -> None:
        """
        添加代码行，可选择性地添加行内注释
        
        Args:
            code_list: 代码列表
            code_line: 代码行（不包含注释）
            comment: 可选的注释内容
        """
        if comment and self._should_include_comments():
            # 提取代码行中的注释部分（如果存在）
            if "//" in code_line:
                # 如果代码行已经包含注释，保留原有注释
                code_list.append(code_line)
            else:
                code_list.append(f"{code_line}\t\t// {comment}")
        else:
            # 不添加注释，只添加代码
            # 移除代码行中可能存在的注释
            clean_line = code_line.split("//")[0].rstrip()
            code_list.append(clean_line)
    
    def _is_chip_1521(self) -> bool:
        """判断当前芯片是否为 JZ8P1521"""
        return self.chip_name == "JZ8P1521"
    
    @abstractmethod
    def generate(self) -> str:
        """
        生成代码
        
        Returns:
            生成的代码字符串
        """
        pass

