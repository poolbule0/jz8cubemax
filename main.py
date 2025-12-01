#!/usr/bin/env python
# -*- coding: gbk -*-
"""
JZ8P2615 代码生成工具 - 主程序入口
类似 STM32 CubeMX 的配置工具
"""

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui import CodeGeneratorUI
from control import ConfigController


def main():
    """主函数"""
    print("=" * 50)
    print("JZ8P2615 代码生成工具")
    print("版本: 1.0.0")
    print("=" * 50)
    
    try:
        # 创建配置控制器
        controller = ConfigController()
        
        # 创建并启动UI
        app = CodeGeneratorUI(controller)
        app.run()
        
    except Exception as e:
        print(f"程序启动失败: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

