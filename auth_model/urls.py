from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'auth_model'

urlpatterns = [
    url(r'^login/$', TemplateView.as_view(template_name='auth_model/login.html'), name='login'), #displays a login page
    url(r'^authenticate/$', views.authenticate_method, name='authenticate_method'),# this method checks for the user with given credentials
    url(r'^success/$', TemplateView.as_view(template_name='auth_model/success.html'), name='success'), # success message after login and logout link
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^create_new_user/$', views.create_new_user, name='create_new_user'), #method to create a new user using the given credentials
    url(r'^sign_up/$', TemplateView.as_view(template_name='auth_model/sign_up.html'), name='sign_up'), # sign up page
]
