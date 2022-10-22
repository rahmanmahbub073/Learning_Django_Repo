from django.shortcuts import render
from .forms import TeacherRegistration


# Create your views here.


def admin(request):
    return render(request, 'Admin/admin.html')


def showformsdata(request):
    tr = TeacherRegistration()
    # tr.order_fields(field_order=['email', 'last_name', 'first_name'])
    if request.method == 'POST':
        tr = TeacherRegistration(request.POST)
        print(tr)
        print("This is post method")
        print(tr.cleaned_data)
    else:
        tr = TeacherRegistration()
        print("This is get Statment")
    return render(request, 'Admin/forms.html', {'forms': tr})
