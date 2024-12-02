#!/bin/bash

echo "Startup the server..."
ufw allow 8000
ufw allow 8001
chmod 777 /server/messenger_server/my-venv/bin/python3
/server/messenger_server/my-venv/bin/python3 manage.py runserver 176.124.204.174:8000 &
echo "Server startup completed!"