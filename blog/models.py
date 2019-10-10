from django.db import models
from django.utils import timezone

#_________________________________________________________________
# ARTICLE 
#_________________________________________________________________

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    slug = models.SlugField(max_length=100)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")

    photo = models.ImageField(upload_to="articles/")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Article"
        ordering = ['date']
    
    def __str__(self):
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100)
    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.nom