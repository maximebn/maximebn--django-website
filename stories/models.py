from django.db import models
from django.utils import timezone


#_________________________________________________________________
# STORY 
#_________________________________________________________________
class Story(models.Model):
    titre = models.CharField(max_length=100)
    sousTitre = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    annee = models.CharField(max_length=40)
    contenu = models.TextField(null=True)
    mapFrameLink = models.TextField(null=False, verbose_name="adresse de la carte OpenStreetMaps pour intégration dans une iFrame")
    mapLink = models.TextField(null=True, verbose_name="lien vers la carte OpenStreetMaps.org")

    slug = models.SlugField(max_length=100)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")

    photo = models.ImageField(upload_to="stories/")    
    class Meta:
        verbose_name = "Story"
        ordering = ['date']
    
    def __str__(self):
        return self.titre

# Here I create an Img class that takes a story as a Foreign key. That means each story can get
# many associated image fields. The using Tabular InLine in admin.py
class Img(models.Model):
    img = models.ImageField(upload_to="stories/") 
    story = models.ForeignKey('Story', on_delete=models.CASCADE)