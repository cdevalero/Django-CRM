from django.contrib import admin
from .models import Client, Service, Sale

admin.site.register([Service, Client, Sale])
