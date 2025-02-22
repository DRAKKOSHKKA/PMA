@echo off
title Python PIP Updater
echo Installing...
pip install -r "requ.txt" > ~temp.tp
del /q "~temp.tp"
cls
echo Installed!
pause
exit
