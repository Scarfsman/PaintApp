from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def mix(request):
    return render(request, 'mix.html')