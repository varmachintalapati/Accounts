@echo off
echo.
echo ==========================================
echo  USERS API - PUBLIC INTERNET ACCESS
echo ==========================================
echo.
echo Choose your option:
echo 1. Make API public instantly (ngrok)
echo 2. Cloud deployment instructions
echo 3. Local development only
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting public deployment...
    python public_deploy.py
) else if "%choice%"=="2" (
    echo.
    echo Cloud Deployment Options:
    echo.
    echo 1. RENDER (FREE): https://render.com
    echo 2. RAILWAY (FREE): https://railway.app  
    echo 3. GOOGLE CLOUD RUN: https://cloud.google.com/run
    echo 4. FLY.IO: https://fly.io
    echo.
    echo See README.md for detailed instructions
    pause
) else if "%choice%"=="3" (
    echo.
    echo Starting local development server...
    python app.py
) else if "%choice%"=="4" (
    echo Goodbye!
    exit /b 0
) else (
    echo Invalid choice. Please try again.
    pause
    goto :eof
)

pause
