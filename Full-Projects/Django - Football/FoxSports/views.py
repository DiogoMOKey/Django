# Class and Function Views
from django.views.generic import TemplateView
# Models, Forms
from django.shortcuts import render
from .models import Stadium, Game

class HomePageView(TemplateView):   # Display diferent apps
    template_name = "home.html"
    
    

# Create your views here.
def game(request):
   if request.method=="POST":
      Url=request.POST['url']
      Game.objects.create(url=Url)

   qr_code=Game.objects.all()
   return render(request,"game.html",{'qr_code':qr_code})