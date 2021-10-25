from django.urls import path
from .views import contact, createContact, createService, sales, service, updateContact, updateSale, viewContact, viewSale, viewService, updateService, serviceStatus, changeServiceStatus, createSale


urlpatterns = [
    path('createService/', createService, name='createService'),
    path('service/', service, name='service'),
    path('viewService/<id>', viewService, name='viewService'),
    path('updateService/<id>', updateService, name='updateService'),
    path('serviceStatus/', serviceStatus, name='serviceStatus'),
    path('changeServiceStatus/<id>', changeServiceStatus, name='changeServiceStatus'),

    path('createSale/', createSale, name='createSale'),
    path('sales/', sales, name='sales'),
    path('viewSale/<id>', viewSale, name='viewSale'),
    path('updateSale/<id>', updateSale, name='updateSale'),

    path('createContact/', createContact, name='createContact'),
    path('contact/', contact, name='contact'),
    path('viewContact/<id>', viewContact, name='viewContact'),
    path('updateContact/<id>', updateContact, name='updateContact'),
]
