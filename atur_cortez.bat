
@echo off
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Meminta izin Administrator...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

set "HOSTS=%SystemRoot%\System32\drivers\etc\hosts"
findstr /i /c:"127.0.0.1 cortez" "%HOSTS%" >nul
if %errorlevel% neq 0 (
    echo 127.0.0.1 cortez>>"%HOSTS%"
)

ipconfig /flushdns
echo.
echo Selesai! Coba jalankan: ping cortez
pause