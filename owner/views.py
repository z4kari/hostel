from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request,'owner/login.html')

def home(request):
    return render(request,'owner/home.html')