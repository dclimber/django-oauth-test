from .base import *

DEBUG = False

ALLOWED_HOSTS = [env('ALLOWED_HOST')]

DATABASES = {
    'default': env.db(),
}

# Email
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

try:
    from .local import *
except ImportError:
    pass
