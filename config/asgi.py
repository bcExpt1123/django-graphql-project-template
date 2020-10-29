"""
ASGI config for {{ project_name }} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from dotenv import load_dotenv
from django.core.asgi import get_asgi_application

load_dotenv()

environment_module = os.getenv("ENVIRONMENT_MODULE", "develop")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"config.settings.{environment_module}")

application = get_asgi_application()
