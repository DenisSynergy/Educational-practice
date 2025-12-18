"""
WSGI config for greeting_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greeting_project.settings')

application = get_wsgi_application()
"""
WSGI конфигурация для проекта greeting_project.

WSGI (Web Server Gateway Interface) - это стандартный интерфейс между
веб-сервером и веб-приложением Python. Этот файл используется для
развертывания приложения на продакшн сервере.
"""

import os

from django.core.wsgi import get_wsgi_application

# Установка модуля настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greeting_project.settings')

# Получение WSGI приложения Django
application = get_wsgi_application()

