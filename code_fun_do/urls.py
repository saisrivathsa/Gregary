from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('auth_model.urls')),
    url(r'^gregary/', include('gregary.urls')),
    url(r'^sample', TemplateView.as_view(template_name='auth_model/sample.html'))
]
