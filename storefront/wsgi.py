"""
WSGI config for storefront project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')

application = get_wsgi_application()

# heroku create daniel-prod
# heroku config:set SECRET_KEY='d)8(nuuw%ry&o0tgfthdz6e$u@fo+skka0iod*=i+gob7xod7$' --app=daniel-prod
# heroku config:set DJANGO_SETTINGS_MODULE = storefront.settings.prod - -app = daniel-prod
