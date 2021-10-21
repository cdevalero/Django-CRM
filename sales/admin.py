from django.contrib import admin
from .models import Client, Service

admin.site.register([Service, Client])
