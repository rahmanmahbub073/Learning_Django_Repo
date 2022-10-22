from django.urls import path
from . import views


urlpatterns = [
    path('deep_learning/', views.deep_learning, name='deep_learning'),
    path('knn/', views.knn, name='knn'),
    path('random_forest/', views.random_forest, name='random_forest'),
    path('ann/', views.ann, name='ann'),
]
