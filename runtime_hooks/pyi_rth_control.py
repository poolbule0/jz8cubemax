# -*- coding: utf-8 -*-
# Runtime hook to ensure control module is available
import sys
import os

# Get current exe directory
if getattr(sys, 'frozen', False):
    # If it's a packaged exe
    base_path = sys._MEIPASS
else:
    # If it's development environment
    base_path = os.path.dirname(os.path.abspath(__file__))

# Ensure control module can be imported
try:
    import control
except ImportError:
    # If import fails, try to add to path
    if base_path not in sys.path:
        sys.path.insert(0, base_path)
    try:
        import control
    except ImportError:
        # If still fails, try to import from current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)

