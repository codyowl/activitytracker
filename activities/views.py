from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from activities.forms import ActivityForm
from activities.models import Activity
from django.contrib import messages

@login_required
def activities_home(request, template='activities/activities_home.html'):
	print "inside"
	msg = []
	if request.method == 'POST':
		form = ActivityForm(request.POST)
		if form.is_valid():
			print "yes form is valid"
			activity_category = form.cleaned_data['activity_category']
			details = form.cleaned_data['details']
			status = form.cleaned_data['status']
			
			activity = Activity(activity_category=activity_category,details=details,status=status)
			activity.user = request.user
			activity.save()
			msg.append("Hurray! new activity added !")
			return HttpResponseRedirect('/dashboard/activities-timeline/')
	else:
		form = ActivityForm()
	context = {
	'form':form,
	'msg':msg,
	}			
	return render_to_response(template, context, context_instance=RequestContext(request))

@login_required
def activities_timeline(request, template='activities/activities_timeline.html'):
	activity = Activity.objects.filter(user=request.user.pk)[::-1]
	return render_to_response(template, {'activity':activity}, context_instance=RequestContext(request))	

@login_required
def activities_summary(request, template='activities/activities_summary.html'):
	return render_to_response(template, context_instance=RequestContext(request))


@login_required
def activity_delete(request, id):
	activity_to_delete = get_object_or_404(Activity, pk=id).delete()
	messages.error(request, 'Document deleted!')
	return HttpResponseRedirect('/dashboard/activities-timeline/')

@login_required
def activities_visuals(request, template='activities/activities_visuals.html'):
	return render_to_response(template)

@login_required
def monthly_summary(request, template='activities/monthly_summary.html'):
	activity = Activity.objects.filter(user=request.user.pk)
	# events_dict = {}
	# events_dict['title'] = []
	# for activities in activity:
	# 	events_dict['title'].append(str(activities.activity_category))
	# print events_dict	
	context = {
	'activity':activity,
	}
	return render_to_response(template, context, context_instance=RequestContext(request))	

#activities sync
@login_required
def activities_sync(request, template='activities/activities_sync.html'):
	return render_to_response(template, context_instance=RequestContext(request))
