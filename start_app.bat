@echo off
start /B python BACKEND\server.py
timeout /t 5 /nobreak
start dist\main.exe