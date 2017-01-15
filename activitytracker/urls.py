from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'activitytracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^registration/$', 'home.views.register', name='register'),
    url(r'^login/$', 'home.views.user_login', name='user_login'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^dashboard/$', 'accounts.views.dashboard_home', name='dashboard_home'),
    url(r'^dashboard/activities/$', 'activities.views.activities_home', name='activities_home'),
    url(r'^dashboard/activities/delete/(?P<id>\d+)/$', 'activities.views.activity_delete', name='activity_delete'),
    url(r'^dashboard/activities-timeline/$', 'activities.views.activities_timeline', name='activities_timeline'),
	#monthly summary
    url(r'^dashboard/monthly-summary/$', 'activities.views.monthly_summary', name='monthly_summary'),

    #visuals
    url(r'^dashboard/activities-visuals/$', 'activities.views.activities_visuals', name='activities_visuals'),

    )
