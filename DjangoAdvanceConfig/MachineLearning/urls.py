from django.urls import path
from . import views


urlpatterns = [
    path('machine_learning/', views.machine_learning, name='machine_learning'),
    path('pyt/', views.pytorch, name='pytorch'),
    path('sk_learn/', views.scikit_learn, name='scikit_learn'),
    path('tf/', views.tensor_flow, name='tensor_flow'),
]
