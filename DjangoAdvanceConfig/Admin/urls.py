from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin_page/', views.admin, name='admin'),
    path('forms/', views.showformsdata),
]
