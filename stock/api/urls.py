from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import (
    IndexView,
)

app_name = 'api'

urlpatterns = [
    url(r'^$', IndexView, name='index'),
]
