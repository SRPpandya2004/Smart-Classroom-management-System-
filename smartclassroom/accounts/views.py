from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashbord.html')

def registration(request):
    return render(request, "registration.html")

def signin(request):
    return render(request, "signin.html")
