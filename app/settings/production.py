
import dj_database_url
from app.settings.base import *

DEBUG = False
# Admins (For sending erros log)
ADMINS = [('Joab Mendes', 'joabe.mdl@gmail.com')]

if bool(os.getenv('HEROKU_ENV', False)):
    # If it's hereku just use the url
    DATABASES['default'] = dj_database_url.config()
else:
    # Makes configuration for other servers
    # postgres config for django
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }


WEBPACK_LOADER['DEFAULT']['STATS_FILE'] = (
    os.path.join(BASE_DIR, 'webpack-production-stats.json')
)
