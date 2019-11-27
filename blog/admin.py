from django.contrib import admin
from .models import Categorie, Article

#_________________________________________________________________
# ARTICLE 
#_________________________________________________________________
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'auteur', 'date')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre', ), }

    fieldsets = (
    # Fieldset 1 : meta-info (titre, auteur…)
   ('Général', {
        'classes': ['collapse',],
        'fields': ('titre', 'auteur', 'categorie', 'slug')
    }),
    # Fieldset 2 : contenu de l'article
    ('Contenu de l\'article', {
       'fields': ('contenu', )
    }),
     # Fieldset 3 : photo illustration de l'article
    ('Photo de l\'article', {
       'fields': ('photo', )
    }),
)

#_________________________________________________________________
# CATEGORIE 
#_________________________________________________________________
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nom', ), }
