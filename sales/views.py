from django.shortcuts import render
from .forms import FormService

def createService(request):
    context = FormService()
    return render(request, 'services/create_service.html', {'context': context})

def service(request):
    return render(request, 'services/services.html')

def viewService(request):
    return render(request, 'services/consult_service.html')