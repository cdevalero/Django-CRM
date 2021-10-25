from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import crmUser


def userLogin(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
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
	return render(request, 'login/recovery.html')