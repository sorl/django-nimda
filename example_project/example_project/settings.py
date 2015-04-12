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
LANGUAGE_CODE = c.get('i18n', 'language_code')
MIDDLEWARE_CLASSES = [k for k, v in c.items('middleware')]
ROOT_URLCONF = c.get('main', 'root_urlconf')
SECRET_KEY = c.get('security', 'secret_key')
STATIC_URL = c.get('media', 'static_url')
TEMPLATE_CONTEXT_PROCESSORS = [k for k, v in c.items('context_processors')]
TEMPLATE_DEBUG = c.getboolean('debug', 'template_debug')
TIME_ZONE = c.get('i18n', 'time_zone')
USE_I18N = c.getboolean('i18n', 'use_i18n')
USE_L10N = c.getboolean('i18n', 'use_l10n')
USE_TZ = c.getboolean('i18n', 'use_tz')
WSGI_APPLICATION = c.get('main', 'wsgi_application')
