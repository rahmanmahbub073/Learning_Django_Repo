from audioop import add
from unicodedata import name
from django.urls import path

from login.views import register
from . import views


urlpatterns = [
    path('', views.index, name='index')
]
