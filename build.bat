@echo off
chcp 65001 >nul
echo ========================================
echo JZ8代码生成工具 - 打包脚本
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python
    pause
    exit /b 1
)

echo 正在检查依赖...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo 开始打包程序...
echo.

python build_exe.py

if errorlevel 1 (
    echo.
    echo 打包失败！
    pause
    exit /b 1
)

echo.
echo ========================================
echo 打包完成！
echo 生成的exe文件位于: dist\JZ8代码生成工具.exe
echo ========================================
pause


