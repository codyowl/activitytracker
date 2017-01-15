from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_home(request, template='accounts/dashboard_home.html'):
	return render_to_response(template, context_instance = RequestContext(request))
