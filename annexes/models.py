from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from maximebn import staticAttributes

#_________________________________________________________________
# ABOUT 
#_________________________________________________________________

class About(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    photo = models.ImageField(upload_to="about/")
    dateCreation = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")
    
    class Meta:
        verbose_name = "A propos - section"
    
    def __str__(self):
        return self.titre
    
    # Here, I only want to create one instance of About (it is unique)
    # Overwrittting save method so that I check if an instance already exists class 

    def save(self, *args, **kwargs):
        if About.objects.exists() and not self.pk:
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError(staticAttributes.ERROR_ANNEXES_ABOUT_VAL)
        return super(About, self).save(*args, **kwargs)

#_________________________________________________________________
# MENTIONS LEGALES 
#_________________________________________________________________

class Mentions(models.Model):
    categorie = models.CharField(max_length=50)
    contenu = models.TextField(null=True)
    dateCreation = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")


    mentionNotFound = staticAttributes.ANNEXES_MENTIONS_NOT_FOUND

    class Meta:
        verbose_name = "Mentions légales - catégorie"

    def __str__(self):
        return self.categorie


#_________________________________________________________________
# DATA POLICY 
#_________________________________________________________________
class Policy(models.Model):
    categorie = models.CharField(max_length=50)
    contenu = models.TextField(null=True)
    dateCreation = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")

    dataNotFound = staticAttributes.ANNEXES_DATA_NOT_FOUND
        
    class Meta:
        verbose_name = "Data policy - catégorie"

    def __str__(self):
        return self.categorie

