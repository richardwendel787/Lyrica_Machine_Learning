@echo on

taskkill /F /IM python.exe

start "C:\Users\Owner\AppData\Local\Programs\Python\Python37\python.exe"  /D "C:\Users\Owner\Desktop\Final Project\Lyrica_Machine_Learning_FP" "C:\Users\Owner\Desktop\Final Project\Lyrica_Machine_Learning_FP\app.py"

start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" "http://127.0.0.1:5000/"