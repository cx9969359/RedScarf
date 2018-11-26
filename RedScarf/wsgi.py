"""
WSGI config for RedScarf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get('RedScarf', None)
if env == 'DEVELOPMENT':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RedScarf.settings.development')
elif env == 'PRODUCT':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RedScarf.settings.production')
else:
    raise EnvironmentError('Environment is error')

application = get_wsgi_application()
