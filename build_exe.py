#!/usr/bin/env python
# -*- coding: gbk-*-
"""
打包脚本 - 将程序打包成exe文件（无控制台窗口）
"""

import os
import sys
import subprocess

# 尝试导入 PyInstaller
try:
    import PyInstaller.__main__  # pyright: ignore[reportMissingModuleSource]
    HAS_PYINSTALLER = True
except ImportError:
    HAS_PYINSTALLER = False

def _fix_spec_file(spec_file: str, current_dir: str):
    """修复 spec 文件，确保 control 模块被包含"""
    try:
        with open(spec_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查 hiddenimports 中是否包含 control
        if "'control'" not in content and '"control"' not in content:
            # 在 hiddenimports 列表中添加 control
            import re
            # 查找 hiddenimports = [...] 的模式
            pattern = r"hiddenimports\s*=\s*\[(.*?)\]"
            match = re.search(pattern, content, re.DOTALL)
            if match:
                imports = match.group(1)
                # 确保 control 在列表中
                if "'control'" not in imports and '"control"' not in imports:
                    # 在列表开头添加 control
                    new_imports = "'control', " + imports.lstrip()
                    content = content[:match.start(1)] + new_imports + content[match.end(1):]
                    # 写回文件
                    with open(spec_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print("已修复 spec 文件，添加了 control 模块")
    except Exception as e:
        print(f"修复 spec 文件时出错（可忽略）: {e}")

def build_exe():
    """打包程序为exe文件"""
    
    # 检查 PyInstaller 是否可用
    if not HAS_PYINSTALLER:
        try:
            # 尝试通过 subprocess 检查 pyinstaller 是否在 PATH 中
            result = subprocess.run([sys.executable, '-m', 'PyInstaller', '--version'], 
                         check=True, capture_output=True, text=True)
            print(f"检测到 PyInstaller: {result.stdout.strip()}")
            # 如果 subprocess 可以运行，说明 PyInstaller 可用，只是导入失败
            # 继续使用 subprocess 方式
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print("=" * 50)
            print("错误: PyInstaller 未安装或不可用")
            print("=" * 50)
            print(f"当前 Python 解释器: {sys.executable}")
            print(f"Python 版本: {sys.version}")
            print()
            print("请使用以下命令安装 PyInstaller:")
            print(f"  {sys.executable} -m pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple")
            print()
            print("或者安装所有依赖:")
            print(f"  {sys.executable} -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple")
            print("=" * 50)
            return 1
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 检查数据目录是否存在
    datasheet_dir = os.path.join(current_dir, "数据手册")
    example_dir = os.path.join(current_dir, "示例项目")
    
    # hooks 目录
    hooks_dir = os.path.join(current_dir, "hooks")
    
    # runtime hooks 目录
    runtime_hooks_dir = os.path.join(current_dir, "runtime_hooks")
    
    # 检查是否已存在 exe 文件
    exe_path = os.path.join(current_dir, "dist", "JZ8代码生成工具.exe")
    if os.path.exists(exe_path):
        print(f"警告: 已存在 exe 文件: {exe_path}")
        print("将继续打包，新文件将覆盖旧文件...")
        print()
    
    # 检查关键文件是否存在
    control_file = os.path.join(current_dir, "control.py")
    ui_file = os.path.join(current_dir, "ui.py")
    if not os.path.exists(control_file):
        print(f"错误: 找不到 control.py 文件: {control_file}")
        return 1
    if not os.path.exists(ui_file):
        print(f"错误: 找不到 ui.py 文件: {ui_file}")
        return 1
    
    # 图标文件路径
    icon_file = os.path.join(current_dir, "app.ico")
    icon_arg = f'--icon={icon_file}' if os.path.exists(icon_file) else '--icon=NONE'
    
    # PyInstaller 参数
    args = [
        'main.py',                    # 主程序入口
        '--name=JZ8代码生成工具',      # 生成的exe文件名
        '--onefile',                  # 打包成单个exe文件
        '--windowed',                 # 无控制台窗口（Windows GUI模式）
        icon_arg,                     # 图标（如果有图标文件可以指定路径）
        f'--paths={current_dir}',     # 添加当前目录到搜索路径（重要！）
        f'--additional-hooks-dir={hooks_dir}',  # 使用自定义 hook 文件
        # 暂时移除运行时 hook，因为编码问题（GBK vs UTF-8）
        # f'--runtime-hook={os.path.join(runtime_hooks_dir, "pyi_rth_control.py")}',  # 运行时 hook
        '--hidden-import=control',     # 显式导入 control 模块（最重要！）
        '--hidden-import=ui',          # 显式导入 ui 模块
        '--collect-all=control',       # 收集 control 模块的所有内容
        '--collect-all=ui',            # 收集 ui 模块的所有内容
        '--hidden-import=tkinter',     # 确保tkinter被包含
        '--hidden-import=tkinter.ttk',
        '--hidden-import=tkinter.scrolledtext',
        '--hidden-import=tkinter.filedialog',
        '--hidden-import=tkinter.messagebox',
        '--collect-all=tkinter',      # 收集所有tkinter相关文件
        '--noupx',                    # 不使用UPX压缩（避免某些问题）
        '--clean',                    # 清理临时文件
        '--log-level=INFO',           # 设置日志级别
    ]
    
    # 添加数据目录（如果存在）
    if os.path.exists(datasheet_dir):
        args.append(f'--add-data={datasheet_dir};数据手册')
    if os.path.exists(example_dir):
        args.append(f'--add-data={example_dir};示例项目')
    
    # 添加所有Python模块到隐藏导入（确保所有本地模块都被包含）
    modules = [
        'control',                    # 顶层模块，必须显式导入
        'ui',                         # 顶层模块，必须显式导入
        'chips',                      # 包
        'chips.chip_base',
        'chips.chip_registry',
        'chips.jz8p1521',
        'chips.jz8p2615',
        'generators',                 # 包
        'generators.base_generator',
        'generators.init_generator',
        'generators.main_generator',
        'generators.isr_generator',
        'generators.sleep_generator',
        'generators.adc_generator',
        'generators.pwm_generator',
        'ui_components',              # 包
        'ui_components.base_component',
        'ui_components.gpio_config',
        'ui_components.adc_config',
        'ui_components.timer_config',
        'ui_components.pwm_config',
        'ui_components.interrupt_config',
        'ui_components.sleep_config',
        'ui_components.isr_config',
        'ui_components.main_config',
        'ui_components.system_config',
        'utils',                      # 包
        'utils.register_calc',
        'utils.file_utils',
        'utils.config_validator',
    ]
    
    for module in modules:
        args.append(f'--hidden-import={module}')
    
    # 使用 collect-submodules 确保所有子模块都被收集
    args.append('--collect-submodules=chips')
    args.append('--collect-submodules=generators')
    args.append('--collect-submodules=ui_components')
    args.append('--collect-submodules=utils')
    
    print("开始打包程序...")
    print("=" * 50)
    print("提示: 打包过程可能需要几分钟，请耐心等待...")
    print("=" * 50)
    print()
    
    try:
        if HAS_PYINSTALLER:
            # 使用 PyInstaller.__main__ 方式
            print("正在使用 PyInstaller 打包...")
            print(f"当前工作目录: {current_dir}")
            print(f"control.py 路径: {control_file}")
            print(f"ui.py 路径: {ui_file}")
            print()
            PyInstaller.__main__.run(args)
        else:
            # 使用 subprocess 调用 pyinstaller 命令
            print("正在使用 subprocess 调用 PyInstaller...")
            print(f"Python 解释器: {sys.executable}")
            print()
            cmd = [sys.executable, '-m', 'PyInstaller'] + args
            result = subprocess.run(cmd, check=True)
            if result.returncode != 0:
                raise Exception(f"PyInstaller 执行失败，返回码: {result.returncode}")
        
        # 检查并修复 spec 文件，确保 control 模块被包含（备用方案）
        spec_file = os.path.join(current_dir, "JZ8代码生成工具.spec")
        if os.path.exists(spec_file):
            _fix_spec_file(spec_file, current_dir)
        
        # 检查 exe 文件是否成功生成
        if os.path.exists(exe_path):
            file_size = os.path.getsize(exe_path)
            file_size_mb = file_size / (1024 * 1024)
            print()
            print("=" * 50)
            print("打包完成！")
            print(f"生成的exe文件位于: {exe_path}")
            print(f"文件大小: {file_size_mb:.2f} MB")
            print("=" * 50)
        else:
            print()
            print("=" * 50)
            print("警告: 打包过程完成，但未找到生成的 exe 文件")
            print("请检查 build 目录和 dist 目录")
            print("=" * 50)
            return 1
    except subprocess.CalledProcessError as e:
        print(f"打包失败: PyInstaller 执行出错")
        print(f"错误信息: {e}")
        import traceback
        traceback.print_exc()
        return 1
    except FileNotFoundError:
        print("错误: 未找到 PyInstaller")
        print("请先安装 PyInstaller: pip install pyinstaller")
        return 1
    except Exception as e:
        print(f"打包失败: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(build_exe())

