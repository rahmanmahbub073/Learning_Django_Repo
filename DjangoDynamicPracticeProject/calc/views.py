from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello Django</h1>")
    return render(request, 'home.html', {'name':'Mahbub'})

def add(request):
    # val1 = int(request.GET['num1'])
    # val2 = int(request.GET['num2'])
    
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    Addresult = val1+val2
    return render(request, 'result.html',{'Res': Addresult}) # http://127.0.0.1:8000/add?num1=2&num2=8

