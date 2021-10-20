from django.shortcuts import render

def test(request):
	return render(request, 'representatives/representatives_user.html')
