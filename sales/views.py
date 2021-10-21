from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormService, FormServiceUpdate
from .models import Service

def service(request):
    context = Service.objects.filter(status= True)
    return render(request, 'services/services.html', {'context': context})


def createService(request):
    form = FormService()
    if request.method == 'POST':
        form = FormService(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'services/create_other_service.html')
        else:
            messages.error(request, 'The information entered is invalid, please check and try again')
            return redirect('createService')

    return render(request, 'services/create_service.html', {'form': form})


def viewService(request, id):
    try:
        context = Service.objects.get(id= id)
    except Service.DoesNotExist:        
        return redirect('service')

    return render(request, 'services/consult_service.html', {'context': context})


def updateService(request, id):
    try:
        row = Service.objects.get(id= id)
    except Service.DoesNotExist:        
        return redirect('service')

    if request.method == 'POST':
        form = FormServiceUpdate(request.POST, instance= row)
        if form.is_valid():
            form.save()
            messages.success(request, 'The data of the service has been updated successfully')
            return redirect('service')
        else:
            messages.error(request, 'The information entered is invalid, please check and try again')

    form = FormServiceUpdate(instance= row)
    return render(request, 'services/create_service.html', {'form': form})


def serviceStatus(request):
    context = Service.objects.all()
    return render(request, 'services/service_status.html', {'context': context})

def changeServiceStatus(request, id):
    try:
        context = Service.objects.get(id= id)
    except Service.DoesNotExist:        
        return redirect('serviceStatus')

    if request.method == 'POST':
        print(context)        

    return render(request, 'services/service_status_change.html', {'context': context})