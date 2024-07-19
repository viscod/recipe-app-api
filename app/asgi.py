"""
ASGI config for _app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgiapplication

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgiapplication()
