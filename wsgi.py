import os.path
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

os.environ['DJANGO_SETTINGS_MODULE'] = 'zoink.settings'
os.environ['FLAVOR'] = 'prod'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
