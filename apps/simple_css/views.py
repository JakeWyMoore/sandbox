from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def buttons(request):
    return render(request, 'buttons.html')

def color_schemes(request):
    return render(request, 'color_schemes.html')