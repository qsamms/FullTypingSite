from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    #path('<int:user_id>/',views.userstats,name = 'userstats'),
    path('post/',views.post_request,name =' posthandler'),
    path('get/',views.get_reqeust, name = 'gethandler')
]

