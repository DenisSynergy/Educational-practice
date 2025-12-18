"""
ASGI конфигурация для проекта greeting_project.

ASGI (Asynchronous Server Gateway Interface) - это асинхронный интерфейс
для веб-приложений Python. Используется для поддержки WebSocket и других
асинхронных протоколов.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greeting_project.settings')

application = get_asgi_application()

