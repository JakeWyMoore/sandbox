from django.shortcuts import render

def index(request):
    return render(request, 'insta_feed.html')
