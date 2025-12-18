"""
Настройки Django для проекта greeting_project.

Этот файл содержит все конфигурационные параметры проекта:
- Настройки базы данных
- Список установленных приложений
- Middleware компоненты
- Настройки безопасности (включая CSRF защиту)
- Настройки шаблонов и статических файлов
"""

from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR - это корневая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# Секретный ключ используется для криптографической подписи
# В продакшене должен храниться в переменных окружения!
SECRET_KEY = 'django-insecure-temporary-key-for-educational-purposes-only'

# SECURITY WARNING: don't run with debug turned on in production!
# Режим отладки: показывает подробные ошибки
# В продакшене должно быть False!
DEBUG = True

# Разрешенные хосты для работы приложения
ALLOWED_HOSTS = []


# Application definition
# Список установленных приложений Django

INSTALLED_APPS = [
    'django.contrib.admin',      # Административный интерфейс Django
    'django.contrib.auth',       # Система аутентификации
    'django.contrib.contenttypes', # Система типов контента
    'django.contrib.sessions',    # Управление сессиями
    'django.contrib.messages',    # Система сообщений
    'django.contrib.staticfiles', # Управление статическими файлами (CSS, JS, изображения)
    'greeting_app',              # Наше приложение для приветствий
]

# Middleware - это компоненты, которые обрабатывают запросы и ответы
# Они выполняются в указанном порядке
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # Безопасность
    'django.contrib.sessions.middleware.SessionMiddleware',    # Управление сессиями
    'django.middleware.common.CommonMiddleware',               # Общие функции
    'django.middleware.csrf.CsrfViewMiddleware',              # ЗАЩИТА ОТ CSRF АТАК
    # CSRF (Cross-Site Request Forgery) защита предотвращает подделку запросов
    # Django автоматически добавляет CSRF токен в формы
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Аутентификация
    'django.contrib.messages.middleware.MessageMiddleware',   # Сообщения
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Защита от clickjacking
]

# Корневой URL-конфигуратор проекта
ROOT_URLCONF = 'greeting_project.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Директория, где Django будет искать шаблоны
        'DIRS': [],
        # Включение автоматического поиска шаблонов в приложениях
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI конфигурация для развертывания приложения
WSGI_APPLICATION = 'greeting_project.wsgi.application'


# Database
# Настройки базы данных
# По умолчанию используется SQLite - легковесная файловая база данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',                   # Путь к файлу базы данных
    }
}


# Password validation
# Валидация паролей (используется для системы аутентификации)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# Настройки интернационализации
LANGUAGE_CODE = 'ru-ru'  # Русский язык

TIME_ZONE = 'Europe/Moscow'  # Часовой пояс

USE_I18N = True  # Включение интернационализации

USE_TZ = True  # Использование часовых поясов


# Static files (CSS, JavaScript, Images)
# Настройки статических файлов
STATIC_URL = 'static/'  # URL префикс для статических файлов

# Default primary key field type
# Тип поля первичного ключа по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

