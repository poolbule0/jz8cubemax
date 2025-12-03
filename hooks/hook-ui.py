# -*- coding: utf-8 -*-
# Hook for ui module
# Ensure ui and control modules and all dependencies are included
from PyInstaller.utils.hooks import collect_all, collect_submodules

# Collect all content from ui module
try:
    datas, binaries, hiddenimports = collect_all('ui')
except:
    datas, binaries, hiddenimports = [], [], []

# Ensure ui and control modules are included
hiddenimports = ['ui', 'control'] + hiddenimports

# Collect all submodules that ui module depends on
try:
    hiddenimports += collect_submodules('ui')
except:
    pass

