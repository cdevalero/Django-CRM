from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import FormEvent, FormEventUpdate
from user.views import loginUnder24h


@login_required
def events(request):
	if loginUnder24h(request):
		return redirect('logout')
	# if request.user.is_staff:
	# 	context = Event.objects.all()
	# else:
	# 	context = Event.objects.filter(id_user= request.user.id)
	context = Event.objects.filter(id_user= request.user.id)
	return render(request, 'calendar/calendar.html', {'context': context})


@login_required
def createEvent(request):
	if loginUnder24h(request):
		return redirect('logout')
	if request.method == 'POST':
		form = FormEvent(request.user,request.POST)
		if form.is_valid() and form.dataValidation(request.user.id):
			form.save()
			return render(request, 'calendar/create_other_event.html')
		else:
			messages.error(request, 'The information entered is invalid, please check and try again')
			return redirect('createEvent')
	form = FormEvent(request.user,initial={'id_user': request.user.id, 'status': 'next'})
	return render(request, 'calendar/create_event.html', {'form': form}) 


@login_required
def updateEvent(request, id):
	if loginUnder24h(request):
		return redirect('logout')
	try:
		row = Event.objects.get(id= id)
	except Event.DoesNotExist:        
		return redirect('events')

	if row.id_user == request.user:
		if request.method == 'POST':
			form = FormEventUpdate(request.user,request.POST,instance= row)
			if form.is_valid() and form.dataValidation():
				form.save()
				messages.success(request, 'The data of the contact has been updated successfully')
				return redirect('events')
			else:
				messages.error(request, 'The information entered is invalid, please check and try again')

		form = FormEventUpdate(request.user,instance= row)
		return render(request, 'calendar/create_event.html', {'form': form})

	messages.error(request, 'You do not have permission to enter')
	return redirect('dashboard')


@login_required
def viewEvent(request, id):
	if loginUnder24h(request):
		return redirect('logout')
	try:
		context = Event.objects.get(id= id)
	except Event.DoesNotExist:        
		return redirect('events')

	if context.id_user == request.user or request.user.admin_user:
		return render(request, 'calendar/consult_event.html', {'context': context})

	messages.error(request, 'You do not have permission to enter')
	return redirect('dashboard')

