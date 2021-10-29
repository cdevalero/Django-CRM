from django.urls import path
from .views import events, viewEvent, updateEvent, createEvent

urlpatterns = [

    path('', events, name='events'),
    path('create/', createEvent, name='createEvent'),
    path('update/<id>', updateEvent, name='updateEvent'),
    path('view/<id>', viewEvent, name='viewEvent'),

]
