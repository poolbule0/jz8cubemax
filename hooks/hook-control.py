# -*- coding: utf-8 -*-
# Hook for control module
# Ensure control module and all dependencies are included
from PyInstaller.utils.hooks import collect_all, collect_submodules

# Collect all content from control module
try:
    datas, binaries, hiddenimports = collect_all('control')
except:
    datas, binaries, hiddenimports = [], [], []

# Ensure control module itself is included
hiddenimports = ['control'] + hiddenimports

# Collect all submodules that control module depends on
try:
    hiddenimports += collect_submodules('control')
except:
    pass

