from django.urls import path
from . import views


urlpatterns = [
    path('data_science/', views.data_science, name='data_science'),
    path('ms/', views.my_sql, name='my_sql'),
    path('py/', views.python, name='python'),
    path('pa/', views.pandas, name='pandas'),
    path('r/', views.R_Prog, name='R_Prog'),
    path('tb/', views.tableau, name='tableau'),
]
