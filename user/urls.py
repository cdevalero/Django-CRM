from django.urls import path
from .views import resendMail, representatives, createRepresentative, updateRepresentative, viewRepresentative, representativeStatus, changeRepresentativeStatus

urlpatterns = [
    path('representatives/', representatives, name='representatives'),
    path('representatives/create/', createRepresentative, name='createRepresentative'),
    path('representatives/view/<id>', viewRepresentative, name='viewRepresentative'),
    path('representatives/update/<id>', updateRepresentative, name='updateRepresentative'),
    path('representatives/status/', representativeStatus, name='representativeStatus'),
    path('representatives/status/change/<id>', changeRepresentativeStatus, name='changeRepresentativeStatus'),
    path('representatives/resend/<id>', resendMail, name='resend'),
]
