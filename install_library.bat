@echo off
title Python PIP Updater
cd..
echo Installing...
pip install -r "requ.txt" > tweaks/~temp.tp
cd tweaks
del /q "~temp.tp"
cls
echo Installed!
pause
exit
