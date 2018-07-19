from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    #Definindo um objeto de nome "Post" *sempre iniciar classe com letra maiuscula

    author         = models.ForeignKey('auth.User',on_delete=models.CASCADE) #link para outro modelo
    title          = models.CharField(max_length=200) #delimitando numeros de caracteres
    text           = models.TextField() #não tem limites de caracteres
    created_date   = models.DateTimeField(        default=timezone.now    ) #hora e data
    published_date = models.DateTimeField(     blank = True, null = True    )

    def publish(self):
        #função de nome publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title