from django import views
from django.urls import path
from .views import game
    

urlpatterns = [
   path('', views.game.as_view(), name='Game'),    
]
