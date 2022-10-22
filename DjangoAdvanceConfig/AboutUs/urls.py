from django.contrib import admin
from django.urls import path
from . import views

#  -m pip install -U autopep8


urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('teacher_info/', views.teacher_info,),

]
