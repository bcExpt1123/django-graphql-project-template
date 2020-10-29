# Built-in packages

# Third-party packages
from django.contrib import admin
from django.urls import path

# Local packages
from config.urls.common import *  # noqa

urlpatterns = [
    path("admin/", admin.site.urls),
]
