from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import crmUser
from .forms import FormRepresentative, FormRepresentativeUpdate
from .email import send_email, resend_email_representative, send_email_update, send_recovery_password

#------------------------------- Login ------------------------------- 

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
	    		crmUser.objects.get(user_email = username)
	    	except crmUser.DoesNotExist:
	    		messages.error(request, 'The email is not registered, check it and try again')
	    	else:
	    		messages.error(request, 'Email or password invalid, check it and try again')
	    	

	if request.user.is_authenticated:
		return redirect('dashboard')


	return render(request, 'login/login.html')


def userLogout(request):
    logout(request)
    return redirect('login')


@login_required
def userDashboard(request):
	if request.user.is_staff:
		return render(request, 'dashboard/admin_dashboard.html')
	else:
		return render(request, 'dashboard/representative_dashboard.html')


def userRecovery(request):
	if request.method == 'POST':
		email = request.POST['email']
		try:
			user = crmUser.objects.get(user_email= email)
		except crmUser.DoesNotExist:        
			return redirect('login')
		send_recovery_password(user)
		return render(request, 'login/send_sms.html')

	return render(request, 'login/recovery.html')

# changePassword

def changePassword(request, email, password):
	try:
		user = crmUser.objects.get(user_email= email)
	except crmUser.DoesNotExist:        
		return redirect('login')
	if user.password != password:
		return redirect('login')

	if request.method == 'POST':
		newPassword = request.POST['password1']
		user.new_password(newPassword)
		return render(request, 'login/success.html')

	return render(request, 'login/change_password.html')

#------------------------------- Representatives ------------------------------- 

@login_required
def representatives(request):
	if request.user.is_staff:
		context = crmUser.objects.filter(status=True, admin_user=False)
		return render(request, 'representatives/representatives.html', {'context': context})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def createRepresentative(request):
	if request.user.is_staff:
		form = FormRepresentative()
		if request.method == 'POST':
			form = FormRepresentative(request.POST)
			if form.is_valid():
				form.save()
				send_email(form)
				messages.success(request, 'New Representative is created successfully , an email has bent sent to the email of the representative registered please verified this information')
				# user_representative = crmUser.objects.get(user_email= form.cleaned_data.get('user_email'))
				user_representative = crmUser.objects.get(user_email= form.get_user())
				return render(request, 'representatives/verify_email.html', {'id': user_representative.id})
			else:
				messages.error(request, 'The information entered is invalid, please check and try again')

		return render(request, 'representatives/create_representative.html', {'form': form})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def updateRepresentative(request, id):
	if request.user.is_staff:
		try:
			row = crmUser.objects.get(id= id)
		except crmUser.DoesNotExist:        
			return redirect('representatives')

		if request.method == 'POST':
			old = row.user_email
			form = FormRepresentativeUpdate(request.POST, instance= row)
			
			if form.is_valid():
				form.save()
				if old != form.cleaned_data.get('user_email'):
					messages.success(request, 'The data has been updated successfully, and a mail with the access to the CRM has been sending to the email of the representative user')
					# user_representative = crmUser.objects.get(user_email= form.cleaned_data.get('user_email'))
					user_representative = crmUser.objects.get(user_email= form.get_user())
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
	if request.user.is_staff:
		try:
			context = crmUser.objects.get(id= id)
		except crmUser.DoesNotExist:        
			return redirect('representatives')

		return render(request, 'representatives/consult_representative.html', {'context': context})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def representativeStatus(request):
	if request.user.is_staff:
		context = crmUser.objects.filter(admin_user=False)
		return render(request, 'representatives/representatives_status.html', {'context': context})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')


@login_required
def changeRepresentativeStatus(request, id):
	if request.user.is_staff:
		try:
			context = crmUser.objects.get(id= id)
		except crmUser.DoesNotExist:        
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
	if request.user.is_staff:
		try:
			user = crmUser.objects.get(id= id)
		except crmUser.DoesNotExist:        
			return redirect('representatives')
		
		resend_email_representative(user)
		messages.success(request, 'an email has bent sent to the email of the representative registered please verified this information')
		return render(request, 'representatives/verify_email.html', {'id': id})
	else:
		messages.error(request, 'You do not have permission to enter')
		return redirect('dashboard')