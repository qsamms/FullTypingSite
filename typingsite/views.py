from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    template = loader.get_template('typingsite/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def post_request(request):
    data = request.POST
    print(data['speed'])
    print(data['user_id'])
    return HttpResponse("POST request recieved")

def get_reqeust(request):
    print("get request received")
    return HttpResponse("GET request recieved")
