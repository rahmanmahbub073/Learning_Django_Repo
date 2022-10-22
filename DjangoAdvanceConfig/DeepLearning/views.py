from django.shortcuts import render

# Create your views here.


def deep_learning(request):
    return render(request, 'DeepLearning/deep_learning.html')


def knn(request):
    return render(request, 'DeepLearning/knn.html')


def random_forest(request):
    return render(request, 'DeepLearning/random_forest.html')


def ann(request):
    return render(request, 'DeepLearning/ann.html')
