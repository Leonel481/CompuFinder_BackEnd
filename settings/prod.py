from .base import *
from myproject.env import BASE_DIR, env

env.read_env(os.path.join(BASE_DIR,'.env'))

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[])

CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with']

CORS_ALLOW_CREDENTIALS = True

DATABASES = {
   "default": {
       "ENGINE": "django.db.backends.postgresql",
       "NAME": env('DB_NAME'),
       "USER": env('DB_USER'),
       "PASSWORD": env('DB_PASSWORD'),
       "HOST": env('HOST'),
       "PORT": env('PORT'),
   }
}


# DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.postgresql",
#        "NAME": "db_compu_finder_prod",
#        "USER": "compu_finder",
#        "PASSWORD": "T@]6=jkX9V]p,D2J",
#        "HOST": "10.128.0.2",
#        "PORT": "5432",
#    }
# }

