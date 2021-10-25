from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def events(request):
    pass


@login_required
def createEvent(request):
	pass 


@login_required
def updateEvent(request, id):
	pass


@login_required
def viewEvent(request, id):
	pass