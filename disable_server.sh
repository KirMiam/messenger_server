#!/bin/bash

echo "Shutdown the server"
ufw deny 8000
ufw deny 8001
pkill -f "python3 manage.py runserver 176.124.204.174:8000"
deactivate
echo "Server shutdown completed!"