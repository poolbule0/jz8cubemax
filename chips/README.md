# 芯片支持模块

本模块提供了多芯片代码生成的抽象架构。

## 架构说明

### ChipBase (芯片基类)
所有芯片实现必须继承 `ChipBase` 类，并实现以下抽象方法：

- `get_chip_name()` - 返回芯片唯一标识
- `get_display_name()` - 返回芯片显示名称
- `get_datasheet_path()` - 返回数据手册路径
- `get_example_path()` - 返回示例项目路径
- `get_header_file_name()` - 返回芯片头文件名
- `get_default_config()` - 返回默认配置

### ChipRegistry (芯片注册表)
管理所有可用的芯片实现，使用单例模式。

## 添加新芯片

### 步骤 1: 创建芯片实现类

在 `chips/` 目录下创建新文件，例如 `jz8p2616.py`:

```python
from .chip_base import ChipBase
from typing import Dict, Any

class JZ8P2616Chip(ChipBase):
    """JZ8P2616 芯片实现类"""
    
    def get_chip_name(self) -> str:
        return "JZ8P2616"
    
    def get_display_name(self) -> str:
        return "JZ8P2616"
    
    def get_datasheet_path(self) -> str:
        return "JZ8P2616-V1.0.md"
    
    def get_example_path(self) -> str:
        return "示例项目_JZ8P2616"
    
    def get_header_file_name(self) -> str:
        return "JZ8P2616.h"
    
    def get_default_config(self) -> Dict[str, Any]:
        """返回 JZ8P2616 的默认配置"""
        return {
            # 根据新芯片的寄存器结构定义配置
            "gpio": {
                # GPIO配置...
            },
            # 其他模块配置...
        }
```

### 步骤 2: 注册芯片

在 `chips/chip_registry.py` 的 `_register_default_chips()` 方法中添加：

```python
def _register_default_chips(self):
    """注册默认芯片"""
    # 注册 JZ8P2615
    jz8p2615 = JZ8P2615Chip()
    self.register_chip(jz8p2615)
    
    # 注册 JZ8P2616
    from .jz8p2616 import JZ8P2616Chip
    jz8p2616 = JZ8P2616Chip()
    self.register_chip(jz8p2616)
```

### 步骤 3: 更新 __init__.py

在 `chips/__init__.py` 中导出新芯片：

```python
from .jz8p2616 import JZ8P2616Chip

__all__ = ['ChipBase', 'JZ8P2615Chip', 'JZ8P2616Chip', 'ChipRegistry']
```

## 注意事项

1. **寄存器映射**: 不同芯片的寄存器地址和定义可能不同，需要在 `get_default_config()` 中正确定义
2. **代码生成**: 如果新芯片的代码生成逻辑与 JZ8P2615 差异很大，可能需要在 `control.py` 中添加芯片特定的代码生成方法
3. **示例项目**: 确保示例项目目录存在，并包含正确的头文件和示例代码
4. **数据手册**: 确保数据手册文件存在

## 当前支持的芯片

- JZ8P2615 (默认)

