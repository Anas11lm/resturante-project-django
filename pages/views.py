from django.shortcuts import render, redirect
from django.conf import settings 
from django.core.mail import send_mail 
from django.core.mail import EmailMessage
# from django.conf import settings 
from django.contrib import messages

def index(request):
	return render(request, 'pages/index.html')

def about(request):
	return render(request, 'pages/about.html')	

def events(request):
	return render(request, 'pages/events.html')

def gallery(request):
	return render(request, 'pages/gallery.html')

def chefs(request):
	return render(request, 'pages/chefs.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		send_mail(
		subject = subject,
		message = message,
		from_email = email,
		recipient_list = ['Youremail@gmail.com'],
		fail_silently = False,
)
		messages.success(request, f'{name} Your message has been sent. Thank you!')
		return redirect('index')
			
			

	else:
		return render(request, 'pages/contact.html')	
	

	
			





