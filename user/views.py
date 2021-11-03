from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from event.models import Event
from sales.models import Sale, Service
from .models import CRMUser
from .forms import FormRepresentative, FormRepresentativeUpdate
from .email import send_email, resend_email_representative, send_email_update, send_recovery_password

#------------------------------- Login ------------------------------- 

def loginUnder24h(request):
	if datetime.now() > request.user.last_login + timedelta(hours=24):
		messages.error(request, 'Your token session has expired, login to the system again')
		return True
	return False
		

def userLogin(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None and user.status:
	        login(request, user)
	        return redirect('dashboard')
	    else:
	    	try:
	    		CRMUser.objects.get(user_email = username)
	    	except CRMUser.DoesNotExist:
	    		messages.error(request, 'The email is not registered, check it and try again')
	    	else:
	    		messages.error(request, 'Email or password invalid, check it and try again')
	    	

	if request.user.is_authenticated:
		return redirect('dashboard')


	return render(request, 'login/login.html')


def userLogout(request):
    logout(request)
    return redirect('login')


def userRecovery(request):
	if request.method == 'POST':
		email = request.POST['email']
		try:
			user = CRMUser.objects.get(user_email= email)
		except CRMUser.DoesNotExist:        
			return redirect('login')
		send_recovery_password(user)
		return render(request, 'login/send_sms.html')

	return render(request, 'login/recovery.html')


def changePassword(request, email, password):
	try:
		user = CRMUser.objects.get(user_email= email)
	except CRMUser.DoesNotExist:        
		return redirect('login')
	if user.password != password:
		return redirect('login')

	if request.method == 'POST':
		newPassword = request.POST['password1']
		user.new_password(newPassword)
		return render(request, 'login/success.html')

	return render(request, 'login/change_password.html')


def kpi_data():
	service_demand = Sale.objects.values('id_service').annotate(count=Count('id_service')).order_by()
	for row in service_demand:
		row['id_service'] = Service.objects.get(id= row['id_service']).name

	sales_representatives = Sale.objects.values('id_representative').annotate(count=Count('id_representative')).order_by()
	for row in sales_representatives:
		row['id_representative'] = CRMUser.objects.get(id= row['id_representative']).user_email

	context = {
		'sales_representatives': sales_representatives,
		'sales_country': Sale.objects.values('country').annotate(count=Count('country')).order_by(),
		'sales_process': Sale.objects.values('process_sale_status').annotate(count=Count('process_sale_status')).order_by(),
		'sales_status': Sale.objects.values('status').annotate(count=Count('status')).order_by(),
		'service_demand': service_demand,
	}
	return context


@login_required
def userDashboard(request):
	if loginUnder24h(request):
		return redirect('logout')
	events = Event.objects.filter(id_user= request.user.id, expiration_event_date__range= [datetime.today(), datetime.today() + timedelta(days=7)])
	if request.user.is_staff:
		kpi = kpi_data()
		return render(request, 'dashboard/admin_dashboard.html', {'events': events, 'kpi': kpi})
	else:
		sales = Sale.objects.all()[:5]
		services = Service.objects.filter(status= True, creation_date__range= [request.user.last_login - timedelta(minutes=1), datetime.today() + timedelta(days=1)])
		return render(request, 'dashboard/representative_dashboard.html', {'events': events, 'sales': sales, 'services': services, 'day': datetime.today()})



#------------------------------- Representatives ------------------------------- 

@login_required
def representatives(request):
	if loginUnder24h(request):
		return redirect('logout')
	if request.user.is_staff:
		context = CRMUser.objects.filter(status=True, admin_user=False)
		return render(request, 'representatives/representatives.html', {'context': context})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def createRepresentative(request):
	if loginUnder24h(request):
		return redirect('logout')
	if request.user.is_staff:
		form = FormRepresentative()
		if request.method == 'POST':
			form = FormRepresentative(request.POST)
			if form.is_valid():
				form.save()
				send_email(form)
				messages.success(request, 'New Representative is created successfully , an email has bent sent to the email of the representative registered please verified this information')
				user_representative = CRMUser.objects.get(user_email= form.get_user())
				return render(request, 'representatives/verify_email.html', {'id': user_representative.id})
			else:
				messages.error(request, 'The information entered is invalid, please check and try again')

		return render(request, 'representatives/create_representative.html', {'form': form})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def updateRepresentative(request, id):
	if loginUnder24h(request):
		return redirect('logout')
	if request.user.is_staff:
		try:
			row = CRMUser.objects.get(id= id)
		except CRMUser.DoesNotExist:        
			return redirect('representatives')

		if request.method == 'POST':
			old = row.user_email
			form = FormRepresentativeUpdate(request.POST, instance= row)
			
			if form.is_valid():
				form.save()
				if old != form.cleaned_data.get('user_email'):
					messages.success(request, 'The data has been updated successfully, and a mail with the access to the CRM has been sending to the email of the representative user')
					user_representative = CRMUser.objects.get(user_email= form.get_user())
					password = user_representative.new_password()
					send_email_update(form, password)
					return render(request, 'representatives/verify_email.html', {'id': user_representative.id})
				else:
					return redirect('representatives')
			else:
				messages.error(request, 'The information entered is invalid, please check and try again')

		form = FormRepresentativeUpdate(instance= row)
		return render(request, 'representatives/create_representative.html', {'form': form})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def viewRepresentative(request, id):
	if loginUnder24h(request):
		return redirect('logout')
	if request.user.is_staff:
		try:
			context = CRMUser.objects.get(id= id)
		except CRMUser.DoesNotExist:        
			return redirect('representatives')

		return render(request, 'representatives/consult_representative.html', {'context': context})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def representativeStatus(request):
	if loginUnder24h(request):
		return redirect('logout')
	if request.user.is_staff:
		context = CRMUser.objects.filter(admin_user=False)
		return render(request, 'representatives/representatives_status.html', {'context': context})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def changeRepresentativeStatus(request, id):
	if loginUnder24h(request):
		return redirect('logout')
	if request.user.is_staff:
		try:
			context = CRMUser.objects.get(id= id)
		except CRMUser.DoesNotExist:        
			return redirect('representativeStatus')

		if request.method == 'POST':
			if context.status:
				messages.success(request, 'The representative User has been Inactivated successfully')
				context.status= False  
			else: 
				messages.success(request, 'The representative User has been Activated successfully')
				context.status= True
			context.save(update_fields=['status'])
			return redirect('representativeStatus')

		return render(request, 'representatives/representatives_status_change.html', {'context': context})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def resendMail(request, id):
	if loginUnder24h(request):
		return redirect('logout')
	if request.user.is_staff:
		try:
			user = CRMUser.objects.get(id= id)
		except CRMUser.DoesNotExist:        
			return redirect('representatives')
		
		resend_email_representative(user)
		messages.success(request, 'an email has bent sent to the email of the representative registered please verified this information')
		return render(request, 'representatives/verify_email.html', {'id': id})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')