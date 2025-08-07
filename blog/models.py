from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre= models.CharField(max_length=200)
    contenu= models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date_publication = models.DateTimeField(auto_now_add=True)
    est_publie = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.titre} -  {self.auteur.username} " # Display title and author username
