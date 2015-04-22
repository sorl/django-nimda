import ConfigParser
import os
from os.path import abspath, dirname, join


here = abspath(dirname(__file__))
CONF_DIR = abspath(join(here, os.pardir, 'conf'))
BASE_DIR = abspath(join(here, os.pardir))


default = join(CONF_DIR, 'default.ini')
env = join(CONF_DIR, '%s.ini' % os.environ.get('DJANGO_ENV', 'development'))
c = ConfigParser.RawConfigParser(allow_no_value=True)
c.optionxform = str
c.read([default, env])


ALLOWED_HOSTS = c.get('security', 'allowed_hosts').split(',')
DATABASES = {'default': dict([(k.upper(), v) for k, v in c.items('database')])}
DEBUG = c.getboolean('debug', 'debug')
INSTALLED_APPS = [k for k, v in c.items('apps')]
INTERNAL_IPS = c.get('security', 'internal_ips').split(',')
LANGUAGE_CODE = c.get('i18n', 'language_code')
MEDIA_ROOT = join(BASE_DIR, c.get('media', 'root'))
MIDDLEWARE_CLASSES = [k for k, v in c.items('middleware')]
ROOT_URLCONF = c.get('main', 'root_urlconf')
SECRET_KEY = c.get('security', 'secret_key')
STATIC_URL = c.get('static', 'url')
TEMPLATES = [{
    'BACKEND': c.get('templates', 'backend'),
    'APP_DIRS': c.getboolean('templates', 'app_dirs'),
    'DIRS': [join(BASE_DIR, d) for d in c.get('templates', 'dirs').split(',')],
    'OPTIONS': {
        'context_processors': [k for k, v in c.items('templates.context_processors')],
        'debug': c.getboolean('templates', 'debug'),
    },
}]
TIME_ZONE = c.get('i18n', 'time_zone')
USE_I18N = c.getboolean('i18n', 'use_i18n')
USE_L10N = c.getboolean('i18n', 'use_l10n')
USE_TZ = c.getboolean('i18n', 'use_tz')
WSGI_APPLICATION = c.get('main', 'wsgi_application')
