@echo off
REM 设置PYTHONPATH为当前目录
set PYTHONPATH=%PYTHONPATH%;%CD%

REM 运行配置编辑器
python -m config_editor.osa_editor