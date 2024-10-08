from .base import *
import os

# os.environ['PGSERVICEFILE'] = '/pg_service.conf'
# SECURITY WARNING: In local, set True for debugging
# DEBUG = True


DATABASES = {
   "default": {
       "ENGINE": "django.db.backends.postgresql",
       "NAME": "db_compu_finder_dev",
       "USER": "useradmin",
       "PASSWORD": "\,l+%jK1Qe'q1?D2",
       "HOST": "35.193.232.106",
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
