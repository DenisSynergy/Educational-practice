"""
Конфигурация приложения greeting_app.

Этот файл содержит настройки приложения Django.
"""

from django.apps import AppConfig


class GreetingAppConfig(AppConfig):
    """
    Класс конфигурации приложения greeting_app.
    
    Определяет настройки и поведение приложения.
    """
    
    # Имя приложения по умолчанию
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Имя приложения
    name = 'greeting_app'

