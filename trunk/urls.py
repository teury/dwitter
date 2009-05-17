from django.conf.urls.defaults import *
from settings import PROJECT_PATH
import os

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    #this line is for static serving files
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(PROJECT_PATH, 'media')}),

    (r'^$', 'views.dashboard'),
    (r'^accounts/profile/$', 'views.dashboard'), #simple, dirty login form hack
    
    (r'^registration/login/$', 'django.contrib.auth.views.login',  {'template_name': 'registration/login.html'}),
    (r'^registration/logout/$', 'django.contrib.auth.views.logout',  {'template_name': 'registration/logout.html'}),

    (r'^dweet/form/$', 'views.dweetForm'), 
)
