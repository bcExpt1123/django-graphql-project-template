"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv()

environment_module =  os.getenv('ENVIROMENT_MODULE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings.{environment_module}')

application = get_wsgi_application()
