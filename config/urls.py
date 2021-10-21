from django.contrib import admin
from django.urls import path
from user.views import test
from sales.views import createService, service, viewService, updateService, serviceStatus, changeServiceStatus

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', service, name='test'),

    path('createService/', createService, name='createService'),
    path('service/', service, name='service'),
    path('viewService/<id>', viewService, name='viewService'),
    path('updateService/<id>', updateService, name='updateService'),
    path('serviceStatus/', serviceStatus, name='serviceStatus'),
    path('changeServiceStatus/<id>', changeServiceStatus, name='changeServiceStatus'),

    
]
