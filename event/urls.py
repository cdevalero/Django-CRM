from django.contrib import admin
from django.urls import path
from .views import events, viewEvent, updateEvent, createEvent

urlpatterns = [

    path('', events, name='events'),
    path('createEvent/', createEvent, name='createEvent'),
    path('updateEvent/<id>', updateEvent, name='updateEvent'),
    path('viewEvent/<id>', viewEvent, name='viewEvent'),

]
