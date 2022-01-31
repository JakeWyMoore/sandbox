from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def buttons(request):
    return render(request, 'buttons.html')