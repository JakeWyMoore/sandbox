from django.shortcuts import render, redirect
from .models import Car

def index(request):
    return render(request, 'index.html')

def result_page(request):
    context = {
        'car': Car.objects.all(),
    }
    return render(request, 'results.html', context)


def create(request):
    if request.method == 'POST':
        new_car = Car.objects.create(
            make = request.POST['make'],
            model = request.POST['model'],
            year = request.POST['year'],
            image = request.FILES['image'],
        )
        print(new_car)
        return redirect('/results')
    
    else:
        return redirect('/')
