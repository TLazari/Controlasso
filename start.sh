#!/bin/bash
echo "==========================================="
echo "🚀 App rodando em: http://127.0.0.1:8000/"
echo "==========================================="
exec gunicorn --bind 0.0.0.0:8000 projeto_controlasso.wsgi:application
