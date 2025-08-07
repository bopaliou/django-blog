from django.db import models

class Article(models.Model):
    titre= models.CharField(max_length=200)
    contenu= models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    est_publie = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.titre)
