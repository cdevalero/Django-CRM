from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormContact, FormContactUpdate, FormService, FormServiceUpdate, FormSale, FormSaleUpdate
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
    if request.user.is_staff:
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
                return redirect('service')

        form = FormServiceUpdate(instance= row)
        return render(request, 'services/create_service.html', {'form': form})
    else:
        messages.error(request, 'You do not have permission to enter')
        return redirect('dashboard')


@login_required
def serviceStatus(request):
    if request.user.is_staff:
        context = Service.objects.all()
        return render(request, 'services/service_status.html', {'context': context})
    else:
        messages.error(request, 'You do not have permission to enter')
        return redirect('dashboard')


@login_required
def changeServiceStatus(request, id):
    if request.user.is_staff:
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
    else:
        messages.error(request, 'You do not have permission to enter')
        return redirect('dashboard')


#------------------------------- Sale ------------------------------- 

@login_required
def sales(request):
    if not request.user.is_staff:
        context = Sale.objects.filter(id_representative= request.user.id)
        return render(request, 'sales/sales.html', {'context': context})
    else:
        messages.error(request, 'You do not have permission to enter')
        return redirect('dashboard')


@login_required
def createSale(request): 
    if not request.user.is_staff:
        if request.method == 'POST':
            form = FormSale(request.user,request.POST)
            if form.is_valid() and form.contract_period() and form.clean_representative(request.user.id, request.user.country) and form.init_status():
                form.save() 
                return render(request, 'sales/create_other_sales.html')
            else:
                messages.error(request, 'The information entered is invalid, please check and try again')

        form = FormSale(request.user,initial={'process_sale_status': 'Registered', 'status': 'in process', 'contract': 'dd-mm-aaaa / dd-mm-aaaa','id_representative': request.user.id, 'country': request.user.country})
        return render(request, 'sales/create_sales.html', {'form': form})
    else:
        messages.error(request, 'You do not have permission to enter')
        return redirect('dashboard')


@login_required
def viewSale(request, id):
    if not request.user.is_staff:
        try:
            context = Sale.objects.get(id= id)
        except Sale.DoesNotExist:        
            return redirect('sales')

        if context.id_representative == request.user:
            return render(request, 'sales/consult_sales.html', {'context': context})

    messages.error(request, 'You do not have permission to enter')
    return redirect('dashboard')


# Working
@login_required
def updateSale(request, id):
    if not request.user.is_staff:
        try:
            row = Sale.objects.get(id= id)
        except Sale.DoesNotExist:        
            return redirect('sales')

        if row.id_representative == request.user:
            if request.method == 'POST':
                form = FormSaleUpdate(request.user,request.POST, instance= row)
                if form.is_valid() and form.contract_period():
                    form.save()
                    messages.success(request, 'The data of the sale has been updated successfully')
                    return redirect('sales')
                else:
                    messages.error(request, 'The information entered is invalid, please check and try again')

            form = FormSaleUpdate(request.user,instance= row, initial={'contract': row.formart_contract()})
            return render(request, 'sales/create_sales.html', {'form': form})

    messages.error(request, 'You do not have permission to enter')
    return redirect('dashboard')


#------------------------------- Client ------------------------------- 

@login_required
def contact(request):
    if request.user.is_staff:
        context = Client.objects.all()
    else:
        context = Client.objects.filter(id_representative=request.user)
    return render(request, 'contact/contact.html', {'context': context})


@login_required
def createContact(request): 
    if not request.user.is_staff:
        if request.method == 'POST':
            form = FormContact(request.POST) 
            if form.is_valid() and form.clean_representative(request.user.id, request.user.country):
                form.save()
                return render(request, 'contact/create_other_contact.html')
            else:
                messages.error(request, 'The information entered is invalid, please check and try again')
                return redirect('createContact')

        form = FormContact(initial={'id_representative': request.user.id, 'country': request.user.country})
        return render(request, 'contact/create_contact.html', {'form': form})
    else:
        messages.error(request, 'You do not have permission to enter')
        return redirect('dashboard')


@login_required
def viewContact(request, id):
    try:
        context = Client.objects.get(id= id)
    except Client.DoesNotExist:        
        return redirect('contact')

    if context.id_representative == request.user or request.user.admin_user:
        return render(request, 'contact/consult_contact.html', {'context': context})

    messages.error(request, 'You do not have permission to enter')
    return redirect('dashboard')


@login_required
def updateContact(request, id):
    if not request.user.is_staff:
        try:
            row = Client.objects.get(id= id)
        except Client.DoesNotExist:        
            return redirect('contact')

        if row.id_representative == request.user:
            if request.method == 'POST':
                form = FormContactUpdate(request.POST, instance= row)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'The data of the contact has been updated successfully')
                    return redirect('contact')
                else:
                    messages.error(request, 'The information entered is invalid, please check and try again')

            form = FormContactUpdate(instance= row)
            return render(request, 'contact/create_contact.html', {'form': form})

    messages.error(request, 'You do not have permission to enter')
    return redirect('dashboard')


