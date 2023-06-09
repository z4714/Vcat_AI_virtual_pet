"""
Django settings for VirtualCat_Web project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-msiz51m2d14v9=vh-o)e9)l!_4e@ea6iamhs_nosgaiubq+$f6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",# 权限管理模块
    "django.contrib.contenttypes",# 内容管理模块
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders", #跨域
    'rest_framework',
    'rest_framework_simplejwt',
    'login',
    'pets',
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    #前后端分离
    #"django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "VirtualCat_Web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'TEMPLATES/html')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "VirtualCat_Web.wsgi.application"


# # Database
# # https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# '''
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# '''
DATABASES = {
     "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vcat',  # 您的数据库名称
        'USER': 'comp3070',  # 3070
        'PASSWORD': 'Setukaifa3070',  # 密码
        #可以改为云数据库
        'HOST': 'rm-cn-20p390qg700142ro.rwlb.rds.aliyuncs.com',  # 数据库地址（默认为 localhost）
        'PORT': '3306',  # 数据库端口号（默认为 3306）
        'OPTIONS': {
              'charset': 'utf8mb4',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
#修改后台系统语言
LANGUAGE_CODE = "zh-hans"
#修改时区
TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # ...
    ],
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'


#CORS
#凡是出现在白名单中的域名，都可以访问后端接口
'''
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8001',
    'http://127.0.0.1:8001',
    'http://192.168.1.101:8001',
)
'''
#运行所有用户访问
CORS_ORIGIN_ALLOW_ALL = True

#指明在跨域访问中，后端是否支持对cookie的操作
CORS_ALLOW_CREDENTIALS = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'