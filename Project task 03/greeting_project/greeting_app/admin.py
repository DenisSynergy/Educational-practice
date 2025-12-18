"""
Административная панель Django для приложения greeting_app.

Этот файл настраивает интерфейс администратора Django,
который позволяет управлять данными через веб-интерфейс.
"""

from django.contrib import admin
from .models import UserName


@admin.register(UserName)
class UserNameAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения модели UserName в административной панели.
    
    Декоратор @admin.register автоматически регистрирует модель в админке.
    """
    
    # Поля, которые будут отображаться в списке записей
    list_display = ['name', 'created_at']
    
    # Поля, по которым можно фильтровать записи
    list_filter = ['created_at']
    
    # Поля, по которым можно искать записи
    search_fields = ['name']
    
    # Поля только для чтения (нельзя редактировать)
    readonly_fields = ['created_at']

