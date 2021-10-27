from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import crmUser
from .forms import FormRepresentative, FormRepresentativeUpdate

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


# Working
def userRecovery(request):
	return render(request, 'login/recovery.html')


#------------------------------- Representatives ------------------------------- 

# https://restcountries.com/v3.1/all

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
				return redirect('representatives')
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
			form = FormRepresentativeUpdate(request.POST, instance= row)
			if form.is_valid():
				form.save()
				messages.success(request, 'The data of the representative user is updated successfully')
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