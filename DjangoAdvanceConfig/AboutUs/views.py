from django.http import HttpResponse
from django.shortcuts import render
from AboutUs.models import Teacher

# Create your views here.


def about_us(request):
    # return HttpResponse ("This text is coming from the About us views")
    return render(request, 'AboutUs/about_us.html')


def teacher_info(request):
    teach = Teacher.objects.all()
    return render(request, 'AboutUs/teacher_info.html', {'thr': teach})
