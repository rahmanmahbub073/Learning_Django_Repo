from django.shortcuts import render

# Create your views here.


def data_science(request):
    return render(request, 'DataScience/data_science.html')


def data_analysis(view):
    def get(self, request):
        return render(request, 'DataScience/forms.html')


def my_sql(request):
    return render(request, 'DataScience/my_sql.html')


def python(request):
    return render(request, 'DataScience/python.html')


def pandas(request):
    return render(request, 'DataScience/pandas.html')


def R_Prog(request):
    return render(request, 'DataScience/R_Prog.html')


def tableau(request):
    return render(request, 'DataScience/tableau.html')
