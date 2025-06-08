

from django.shortcuts import render

def assignments(request):
    return render(request, 'assignments.html')

def upload(request):
    return render(request, 'assignment3.html')