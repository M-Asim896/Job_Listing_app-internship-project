@echo off
echo 🚀 Starting Flask Backend...

REM Start Flask backend
start cmd /k "cd backend && ..\venv\Scripts\activate && python app.py"

timeout /t 2

echo 🎯 Starting React Frontend...

REM Start React frontend
start cmd /k "cd frontend && npm start"

echo ✅ Both servers started successfully!
pause
