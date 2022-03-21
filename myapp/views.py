from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
	x = Contact.objects.all()
	form = ContactRegister()
	if request.method == 'POST':
		form = ContactRegister(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'your message received to us successfully')
			return redirect('home')
	context = {
	'x':x,
	'form':form
	}
	return render(request, 'myapp/home.html',context)

def signin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		user = authenticate(username=username,password=password1)

		if user is not None:
			login(request,user)
			
			return render(request,'myapp/home.html')

		else:
			messages.error(request,'Bad authenticate')
			return redirect('signin')


	return render(request,'myapp/signin.html')