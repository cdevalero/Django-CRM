from django.urls import path
from .views import resendMail, representatives, createRepresentative, updateRepresentative, viewRepresentative, representativeStatus, changeRepresentativeStatus

urlpatterns = [
    path('representatives/', representatives, name='representatives'),
    path('createRepresentative/', createRepresentative, name='createRepresentative'),
    path('viewRepresentative/<id>', viewRepresentative, name='viewRepresentative'),
    path('updateRepresentative/<id>', updateRepresentative, name='updateRepresentative'),
    path('representativeStatus/', representativeStatus, name='representativeStatus'),
    path('changeRepresentativeStatus/<id>', changeRepresentativeStatus, name='changeRepresentativeStatus'),
    path('resend/<id>', resendMail, name='resend'),
]
