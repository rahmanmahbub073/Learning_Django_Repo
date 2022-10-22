from django.shortcuts import render

# Create your views here.


def machine_learning(request):
    return render(request, 'MachineLearning/machine_learning.html')


def pytorch(request):
    return render(request, 'MachineLearning/pytorch.html')


def scikit_learn(request):
    return render(request, 'MachineLearning/scikit_learn.html')


def tensor_flow(request):
    return render(request, 'MachineLearning/tensor_flow.html')
