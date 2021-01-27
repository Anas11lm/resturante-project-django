from django.shortcuts import render,redirect
from django.conf import settings 
from django.core.mail import send_mail 
from django.core.mail import EmailMessage
# from django.conf import settings 
from django.contrib import messages
from .models import *

# Create your views here.

def menu(request):
	menus = Specialty.objects.all()
	starts = Start.objects.all()
	salads = Salad.objects.all()
	return render(request, 'menu/menu.html', {'menus':menus,'starts':starts, 'salads':salads})

def specials(request):
	return render(request, 'menu/specials.html')

def book(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		date = request.POST['date']
		people = request.POST['people']
		time = request.POST['time']
		message = request.POST['message']
		send_mail(
		subject = 'This a table Book',
		message = f'the date is: {date}\nthe time is: {time}\npeople are: {people}\nthe phone is: {phone},\nthe message is: {message}',
		from_email = email,
		recipient_list = ['Youremail@gmail.com'],
		fail_silently = False,
		)

		messages.success(request, f'{name} Your Reserve has been sent. Thank you!')
		return redirect('index')
	else:	
		return render(request, 'menu/book.html')	
