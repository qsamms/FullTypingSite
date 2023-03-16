from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.template import loader
from .forms import RegisterForm
from .models import Game

# Create your views here.
def get_homepage(request):
    if request.user.is_authenticated:
        template = loader.get_template('typingsite/home.html')
        allUserGames = Game.objects.filter(user_id = request.user)
        gamelist = list(allUserGames)
        numGames = len(gamelist)
        formattedAvg = formattedAverage(gamelist)
        context = {
            'averagewpm': formattedAvg
        }
        return HttpResponse(template.render(context,request))
    
    return render(request, 'typingsite/home.html')

def post_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            g = Game(user_id = request.user, speed = data['speed'], gametype = data['numwords'])
            g.save()
            return HttpResponse("data saved")
    else:
        return HttpResponse("no user logged in")
    
def formattedAverage(gamelist):
    length = len(gamelist)
    if length == 0: 
        return 0
    else:
        sum = 0
        for game in gamelist:
            sum = sum + game.speed
        avg = sum / length
        return "{:.1f}".format(avg)
    
def findMax(gamelist):
    if len(gamelist) == 0:
        return 0
    max = -1

    for game in gamelist:
        if game.speed > max:
            max = game.speed
    
    return max

def userstats(request):
    template = loader.get_template('typingsite/userstats.html')
    allUserGames = Game.objects.filter(user_id = request.user)
    gamelist = list(allUserGames)
    numGames = len(gamelist)
    formattedAvg = formattedAverage(gamelist)

    tenWordGames = Game.objects.filter(user_id = request.user, gametype = 10)
    gamelist = list(tenWordGames)
    tenGames = len(gamelist)
    tenAvg = formattedAverage(gamelist)
    tenBest = findMax(gamelist)

    twentyfiveWordGames = Game.objects.filter(user_id = request.user, gametype = 25)
    gamelist = list(twentyfiveWordGames)
    twentyfiveGames = len(gamelist)
    twentyfiveAvg = formattedAverage(gamelist)
    twentyfiveBest = findMax(gamelist)

    fiftyWordGames = Game.objects.filter(user_id = request.user, gametype = 50)
    gamelist = list(fiftyWordGames)
    fiftyGames = len(gamelist)
    fiftyAvg = formattedAverage(gamelist)
    fiftyBest = findMax(gamelist)


    context = {
        'averagewpm': formattedAvg,
        'tenAvg': tenAvg,
        'tenBest':tenBest,
        'tenGames': tenGames, 
        'twentyfiveAvg': twentyfiveAvg,
        'twentyfiveBest': twentyfiveBest,
        'twentyfiveGames': twentyfiveGames,
        'fiftyAvg': fiftyAvg,
        'fiftyBest': fiftyBest,
        'fiftyGames': fiftyGames,
        'numgames': numGames
    }
    return HttpResponse(template.render(context,request))

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

