# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all

datas = [('d:\\脚本\\jz8-cubmax\\数据手册', '数据手册'), ('d:\\脚本\\jz8-cubmax\\示例项目', '示例项目')]
binaries = []
hiddenimports = ['control', 'ui', 'tkinter', 'tkinter.ttk', 'tkinter.scrolledtext', 'tkinter.filedialog', 'tkinter.messagebox', 'control', 'ui', 'chips', 'chips.chip_base', 'chips.chip_registry', 'chips.jz8p1521', 'chips.jz8p2615', 'generators', 'generators.base_generator', 'generators.init_generator', 'generators.main_generator', 'generators.isr_generator', 'generators.sleep_generator', 'generators.adc_generator', 'generators.pwm_generator', 'ui_components', 'ui_components.base_component', 'ui_components.gpio_config', 'ui_components.adc_config', 'ui_components.timer_config', 'ui_components.pwm_config', 'ui_components.interrupt_config', 'ui_components.sleep_config', 'ui_components.isr_config', 'ui_components.main_config', 'ui_components.system_config', 'utils', 'utils.register_calc', 'utils.file_utils', 'utils.config_validator']
hiddenimports += collect_submodules('chips')
hiddenimports += collect_submodules('generators')
hiddenimports += collect_submodules('ui_components')
hiddenimports += collect_submodules('utils')
tmp_ret = collect_all('control')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('ui')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('tkinter')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['main.py'],
    pathex=['d:\\脚本\\jz8-cubmax'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=['d:\\脚本\\jz8-cubmax\\hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='JZ8代码生成工具',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['d:\\脚本\\jz8-cubmax\\app.ico'],
)
