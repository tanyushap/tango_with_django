"""
WSGI config for tango_with_django_project project from Tanya Pavlova, 2068010p UofG.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
