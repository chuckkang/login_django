from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	
	return render(request, "login/index.html")



def login(request):
	#check the login credentials
	email = request.POST['email'].strip().lower()
	password = request.POST['password'].strip()
	validlogin = User.objects.login_validation(request.POST)
	if validlogin == True:
		messages.add_message(request, messages.INFO, "You have logged in successfully!")
		user = User.objects.get(email=email)
		request.session['user_id'] = user.id
		return redirect('/success')
	else:
		messages.add_message(request, messages.INFO, validlogin)
		return redirect('/')
	

def register(request):
	if request.method=='POST':
		error = User.objects.registration_validation(request.POST)
		if len(error)!=0:
			# for tag, error in error.iteritems():
			# 	messages.error(request, error, extra_tags=tag)
			# 	print tag, error
			messages.add_message(request, messages.INFO, error)
		else:
			first_name = request.POST['first_name'].strip()
			last_name = request.POST['last_name'].strip()
			email = request.POST['email'].strip().lower()
			password = request.POST['password'].strip()
			password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			user_id = User.objects.create(first_name=first_name , last_name=last_name, email=email , password=password)
			if (user_id.id):
				messages.add_message(request, messages.INFO, "You registered succesfully!")
				request.session['user_id'] = user_id.id
			return redirect('/success')
	else:
		messages.add_message(request, messages.INFO, "You must first login to access this site")
		request.session.clear()
		
	return redirect('/')
def success(request):
	context = {
	'user' : User.objects.get(id=request.session['user_id'])
	}
	#gather the data from the session
	return render(request, 'login/success.html', context)

def logout(request):
	request.session['user_id']=0
	return redirect('/')

def check_session(request):
	if 'user_id' not in request.session:
		request.session.clear()
		return redirect('/')
	
	