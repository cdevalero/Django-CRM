from django.urls import path
from .views import contact, createContact, createService, sales, service, updateContact, updateSale, viewContact, viewSale, viewService, updateService, serviceStatus, changeServiceStatus, createSale


urlpatterns = [
    path('service/create/', createService, name='createService'),
    path('service/', service, name='service'),
    path('service/view/<id>', viewService, name='viewService'),
    path('service/update/<id>', updateService, name='updateService'),
    path('service/status/', serviceStatus, name='serviceStatus'),
    path('service/change_status/<id>', changeServiceStatus, name='changeServiceStatus'),

    path('sales/create/', createSale, name='createSale'),
    path('sales/', sales, name='sales'),
    path('sales/view/<id>', viewSale, name='viewSale'),
    path('sales/update/<id>', updateSale, name='updateSale'),

    path('contact/create/', createContact, name='createContact'),
    path('contact/', contact, name='contact'),
    path('contact/view/<id>', viewContact, name='viewContact'),
    path('contact/update/<id>', updateContact, name='updateContact'),
]
