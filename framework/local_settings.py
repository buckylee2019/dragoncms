import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'k@8#g3)#=vnth3_jbee7ck3r)d810z1s=3611-20c#w(8p74##'

DEBUG = True

ALLOWED_HOSTS = "*"

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ibmcms',
        'USER': 'ibmcms_user',
        'PASSWORD': 'Bph4TCO1M4uElPliiQHLF5NoC1EZdaHc',
        'HOST': 'dpg-ci3igvjhp8u1a18trkb0-a',
        'PORT': '5432'
    }
}
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'EMAIL_HOST'
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
GITLAB_TOKEN = 'GITLAB_TOKEN'
GITHUB_TOKEN = 'GITHUB_TOKEN'
CLOUDFLARE_TOKEN = 'CLOUDFLARE_TOKEN'
CLOUDFLARE_ZONE_ID = 'CLOUDFLARE_ZONE_ID'
TELEGRAM_BOT_TOKEN = 'TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'TELEGRAM_CHAT_ID'
