
from django.contrib import admin
from django.urls import path
from user.views import test
from sales.views import createService

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test, name='test'),
    path('createService/', createService, name='createService'),
]
