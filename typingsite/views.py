from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Game

# Create your views here.
def get_homepage(request):
    return render(request, 'typingsite/home.html')

def post_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            wpm = data['speed']
            g = Game(user_id = request.user, speed = wpm)
            g.save()
            return HttpResponse("data saved")
    else:
        return HttpResponse("no user logged in")

def get_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
    return HttpResponse("GET request recieved")

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

