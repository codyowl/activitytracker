from django.shortcuts import render_to_response, render
from accounts.forms import UserForm 
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
import hashlib
import random
from accounts.models import Profile
from accounts.forms import LoginForm

import datetime

def home(request, template="home/home.html"):
	return render_to_response(template)

def register(request, template="home/register.html"):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			user = User(username=username, email=email,
						first_name=first_name)
			user.set_password(password)
			# user.is_active = False
			user.save()
			#for generaring confirmation link
			# salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
			# usernamesalt = username
			# if isinstance(usernamesalt, unicode):
			#   usernamesalt = usernamesalt.encode('utf8')
			# activation_key = hashlib.sha1(salt+usernamesalt).hexdigest()    

			# profile=Profile()
			# profile.user=user
			# profile.activation_key=activation_key
			# profile.key_expires=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
			# profile.save()
			
			return HttpResponseRedirect('/login')
	else:
		form = UserForm()        
	return render_to_response(template, {'form':form}, context_instance = RequestContext(request)) 


# def user_login(request,template='home/login.html'):
#   msg = []
#   if request.method == 'POST':
#       username = request.POST.get('username')
#       password = request.POST.get('password')
#       user = authenticate(username=username, password=password)
#       if user:
#           if user.is_active:
#               login(request, user)
#               return HttpResponseRedirect('/dashboard/')
#           else:
#               msg.append("Your Daily Journal account is disabled.")
#       else:
#           msg.append("Invalid login details provided.")
#   return render_to_response(template, {"errors":msg}, context_instance = RequestContext(request))

def user_login(request, template='home/login.html'):
	msg = []
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			driver = authenticate(username=username, password=password)
			if driver is not None:
				login(request, driver)
				return HttpResponseRedirect('/dashboard')
			else:
				msg.append("Invalid login details provided")
				return render_to_response(template, {'form': form, 'errors':msg}, context_instance=RequestContext(request))
		
		else:
			return render_to_response(template, {'form': form}, context_instance=RequestContext(request))
	else:
		form = LoginForm()
		context = {'form': form}
		return render_to_response(template, context, context_instance=RequestContext(request))