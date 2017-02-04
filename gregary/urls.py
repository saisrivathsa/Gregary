from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

app_name = 'gregary'

urlpatterns = [
url(r'^$', TemplateView.as_view(template_name='gregary/index.html'), name='index'),
url(r'^auth/', include('auth_model.urls')),
url(r'^register_event/$', TemplateView.as_view(template_name='gregary/register_event.html'), name='register_event'),
url(r'^event_create/$', views.event_create, name='event_create'),
url(r'^events/$', views.coming_events, name='coming_events'),
url(r'^vinam_sample/$', TemplateView.as_view(template_name='gregary/login_redirect.html'), name='vinam_sample'),
]
