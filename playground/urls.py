from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),

]
