from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormContact, FormService, FormServiceUpdate, FormSale
from .models import Client, Service, Sale


#------------------------------- Service ------------------------------- 
@login_required
def service(request):
    context = Service.objects.filter(status= True)
    return render(request, 'services/services.html', {'context': context})


@login_required
def createService(request):
    if request.user.is_staff:
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
    else:
        messages.error(request, 'You do not have permission to enter')
        return redirect('dashboard')


@login_required
def viewService(request, id):
    try:
        context = Service.objects.get(id= id)
    except Service.DoesNotExist:        
        return redirect('service')

    return render(request, 'services/consult_service.html', {'context': context})


@login_required
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


@login_required
def serviceStatus(request):
    context = Service.objects.all()
    return render(request, 'services/service_status.html', {'context': context})


@login_required
def changeServiceStatus(request, id):
    try:
        context = Service.objects.get(id= id)
    except Service.DoesNotExist:        
        return redirect('serviceStatus')

    if request.method == 'POST':
        if context.status:
            messages.success(request, 'The service has been Inactivated successfully')
            context.status= False  
        else: 
            messages.success(request, 'The service has been Activated successfully')
            context.status= True
        context.save(update_fields=['status'])
        return redirect('serviceStatus')

    return render(request, 'services/service_status_change.html', {'context': context})

#------------------------------- Sale ------------------------------- 

@login_required
def sales(request):
    context = Sale.objects.all()
    return render(request, 'sales/sales.html', {'context': context})


# Working
@login_required
def createSale(request): 
    if request.method == 'POST':
        form = FormSale(request.POST)
        if form.is_valid():
            pass
            # form.save()
            # return render(request, 'sales/create_other_sales.html')
    form = FormSale(initial={'process_sale_status': 'Registered', 'status': 'in process'})
    return render(request, 'sales/create_sales.html', {'form': form})


@login_required
def viewSale(request):
    try:
        context = Sale.objects.get(id= id)
    except Sale.DoesNotExist:        
        return redirect('sales')

    return render(request, 'sales/consult_sales.html', {'context': context})


# Working
@login_required
def updateSale(request):
    try:
        row = Sale.objects.get(id= id)
    except Sale.DoesNotExist:        
        return redirect('sales')

    if request.method == 'POST':
        form = FormSale(request.POST, instance= row)
        if form.is_valid():
            # form.save()
            messages.success(request, 'The data of the sale has been updated successfully')
            return redirect('sales')
        else:
            messages.error(request, 'The information entered is invalid, please check and try again')

    form = FormSale(instance= row)
    return render(request, 'sales/update_sales.html', {'form': form})


#------------------------------- Client ------------------------------- 

@login_required
def contact(request):
    context = Client.objects.all()
    return render(request, 'contact/contact.html', {'context': context})


# Working
@login_required
def createContact(request): 
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            pass
            # form.save()
            # return render(request, 'contact/create_other_contact.html')

    form = FormContact(initial={'id_representative': 1, 'country': 'Venezuela'})
    return render(request, 'contact/create_contact.html', {'form': form})


@login_required
def viewContact(request):
    try:
        context = Client.objects.get(id= id)
    except Client.DoesNotExist:        
        return redirect('contact')

    return render(request, 'contact/consult_contact.html', {'context': context})


# Working
@login_required
def updateContact(request):
    try:
        row = Client.objects.get(id= id)
    except Client.DoesNotExist:        
        return redirect('contact')

    if request.method == 'POST':
        form = FormContact(request.POST, instance= row)
        if form.is_valid():
            # form.save()
            messages.success(request, 'The data of the contact has been updated successfully')
            return redirect('contact')
        else:
            messages.error(request, 'The information entered is invalid, please check and try again')

    form = FormContact(instance= row)
    return render(request, 'contact/update_contact.html', {'form': form})

