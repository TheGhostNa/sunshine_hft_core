@echo off
cd /d C:\Users\nirik\OneDrive\Desktop\sunshine_hft\sunshine_hft_core
call .venv\Scripts\activate.bat
python -m dashboard.auto_report_runner
