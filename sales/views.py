from django.shortcuts import render
from .forms import FormService

def createService(request):
    context = FormService()
    return render(request, 'services/create_service.html', {'context': context})
