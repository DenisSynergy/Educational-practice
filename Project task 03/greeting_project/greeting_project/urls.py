"""
URL конфигурация для проекта greeting_project.

Этот файл определяет маршруты (URL patterns) для всего проекта.
Django использует этот файл для определения, какое представление (view)
должно обрабатывать каждый URL запрос.
"""

from django.contrib import admin
from django.urls import path, include

# Список URL паттернов проекта
urlpatterns = [
    # Административный интерфейс Django
    # Доступен по адресу /admin/
    path('admin/', admin.site.urls),
    
    # Включение URL-ов из приложения greeting_app
    # Все URL из greeting_app.urls будут доступны с префиксом /
    # Это позволяет организовать URL-ы по приложениям
    path('', include('greeting_app.urls')),
]
