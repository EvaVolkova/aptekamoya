"""
WSGI config for aptekamoya project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from django.contrib.auth.decorators import login_required

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aptekamoya.settings")

application = get_wsgi_application()
