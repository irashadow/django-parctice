from .base import *

SECRET_KEY = '-otnu!+)3ha7rfaz6a+)=u_-^$z%svludsrk6#&z!-j+eodi0)'
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}