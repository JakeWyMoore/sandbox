from django.shortcuts import redirect, render
from .models import *

def index(request):
    return render(request, 'login_reg.html')

def dashboard(request):
    if 'user_id' in request.session:
        logged_user = User.objects.get(id = request.session['user_id'])
        context = {
            'user': logged_user,
            'images': logged_user.user_images.all()
        }
        print(logged_user.user_images.all())
        print(logged_user.username)

        return render(request, 'insta_feed.html', context)
    else:
        return redirect('/insta-feed')

def login_logic(request):
    if request.method == 'POST':
        logged_user = User.objects.filter(username = request.POST['username'])

        request.session['user_id'] = logged_user[0].id

        return redirect('/insta-feed/dashboard')
    else:
        return redirect('/insta-feed')

def reg_logic(request):
    if request.method == 'POST':
        new_user = User.objects.create(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password'],
        )

        request.session['user_id'] = new_user.id

        return redirect('/insta-feed/dashboard')
    else:
        return redirect('/insta-feed')

def logout(request):
    request.session.flush()
    return redirect('/insta-feed')


def add_image(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            logged_user = User.objects.get(id = request.session['user_id'])
            new_image = Images.objects.create(
                uploader = logged_user,
                image = request.FILES['image']
            )
            print('uploaded')
            return redirect('/insta-feed/dashboard')
        else:
            return redirect('/insta-feed/dashboard')
    else:
        return redirect('/insta-feed')
        
