from django.db import models
import string, random
from django.utils.translation import gettext_lazy as _
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Game.objects.filter(code=code).count() == 0:
            break
    return code



class Stadium(models.Model):
    name = models.TextField(max_length=8, unique=True)
    seats_capacity= models.IntegerField(null=False, default=3000)
    localitation = models.TextField(max_length=20, unique=True)
    open = models.BooleanField(null=False, default=True)
    photo = models.ImageField(null=True, upload_to ='images/')


# Create your models here.
class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    team1 = models.CharField(max_length=20)
    team2 = models.CharField(max_length=20)
    number_tickets = models.IntegerField(null=False, default=1)
    game_finished = models.BooleanField(null=False, default=False)
    url=models.URLField()
    image=models.ImageField(upload_to='qrcode',blank=True)

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.url)
        canvas=Image.new("RGB", (300,300),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)



















  

class Game_Client(models.Model):
    
    class State_choices(models.TextChoices):
        NORMAL = 'NO', _('Normal')
        CLIENT = 'CL', _('Clients')
        URGENT = 'UR', _('Urgent')

    ticket_type = models.CharField(max_length=2, choices=State_choices.choices,
                                    default=State_choices.NORMAL,)
    created_at = models.DateTimeField(auto_now_add=True)
    n_tickets = models.IntegerField(null=False, default=1)
    invite_code = models.CharField(max_length=8, default=generate_unique_code, unique=True)


    def has_priority(self):
        return self.ticket_type in {
            self.State_choices.CLIENT,
            self.State_choices.URGENT,
        }



    
    
class Client_Tickets(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
class State(models.Model):
    aceite = models.CharField(max_length=50, unique=True)






# models.CharField(max_length=8, default=generate_unique_code, unique=True)
  #  accao = models.ForeignKey(TipoAccao_ST, null=True, blank=True ,on_delete=models.CASCADE)

