@echo off
echo =============================================
echo Starting HTTP server on port 8000...
echo =============================================
start "HTTP Server - Port 8000" cmd /k python -m http.server 8000

echo ==============================================
echo Starting listener.py...
echo ==============================================
start "X-Plane Listener Script" cmd /k python C:\xplane_live_map\listener.py
start microsoft-edge:http://localhost:8000
echo If you use another web browser, you can access the Map http://localhost:8000

echo ==============================================
echo All process have been started.
echo Press any key to close this window.
pause

