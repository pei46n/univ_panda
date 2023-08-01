from django import urls
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/stadium/')),
    path('stadium/', include('stadium.urls')),
]
