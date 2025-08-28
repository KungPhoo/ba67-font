@echo off
rem call "C:\Program Files (x86)\FontForgeBuilds\fontforge-console.bat"


set FF=C:\Program Files (x86)\FontForgeBuilds
set AUTOTRACE=%FF%\lib\autotrace-0.31.1-w32
set "PYTHONHOME=%FF%"

set "PATH=%FF%;%FF%\bin;%AUTOTRACE%;%PATH:"=%"



rem for /F "tokens=* USEBACKQ" %%f IN (`dir /b "%FF%lib\python*"`) do (
rem set "PYTHONPATH=%FF%lib\%%f"
rem )

rem PYTHONPATH=%FF%\lib\python3.10
rem PYTHONHOME=%FF%\lib\python3.10

set AUTOTRACE=autotrace.exe
set POTRACE=potrace.exe
set FONTFORGE_VERBOSE=1

call ffpython "%~dp0convert.py"
dir
pause
