from .base import *
import os

# os.environ['PGSERVICEFILE'] = '/pg_service.conf'
# SECURITY WARNING: In local, set True for debugging
# DEBUG = True


DATABASES = {
   "default": {
       "ENGINE": "django.db.backends.postgresql",
       "NAME": "db_compu_finder_dev",
       "USER": "compu_finder",
       "PASSWORD": "T@]6=jkX9V]p,D2J",
       "HOST": "10.128.0.2",
       "PORT": "5432",
   }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "OPTIONS": {
#             "service": 'my_service',
#             'passfile': '.my_pgpass',
#         },
#     }
# }
