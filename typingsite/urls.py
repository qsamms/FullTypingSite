from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.get_homepage, name = 'homepage'),
    path('userstats/',views.userstats,name = 'userstats'),
    path('post/',views.post_request, name =' posthandler'),
    path('get/',views.get_request, name = 'gethandler'),
    path('', include('django.contrib.auth.urls')),
    path('home',views.get_homepage, name = 'homepage'),
    path('sign-up',views.sign_up, name = 'sign-up'),
]