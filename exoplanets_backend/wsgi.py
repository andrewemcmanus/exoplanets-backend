"""
WSGI config for exoplanets_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
# project_folder = os.path.expanduser('../exoplanets_backend')  # a
# load_dotenv(os.path.join(exoplanets_backend, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exoplanets_backend.settings')

application = get_wsgi_application()
