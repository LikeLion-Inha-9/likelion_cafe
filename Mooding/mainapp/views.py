from django.shortcuts import render

# Create your views here.
def intro(request) :
    return render(request, 'intro.html')

def home(request) :
    return render(request, 'home.html')

def like(request) :
    return render(request, 'like.html')

def reserve(request) :
    return render(request, 'reserve.html')

def mypage(request) :
    return render(request, 'mypage.html')

def allcafe(request) :
    return render(request, 'allcafe.html')