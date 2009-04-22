from django.conf.urls.defaults import *

urlpatterns = patterns('',

    (r'^$', 'views.dashboard'),
    (r'^registration/login/$', 'django.contrib.auth.views.login',  {'template_name': 'registration/login.html'}),
    (r'^registration/logout/$', 'django.contrib.auth.views.logout',  {'template_name': 'registration/logout.html'}),
)
