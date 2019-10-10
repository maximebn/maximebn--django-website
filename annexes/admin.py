from django.contrib import admin
from annexes.models import Mentions, About, Policy


#_________________________________________________________________
# MENTIONS 
#_________________________________________________________________
@admin.register(Mentions)
class MentionsAdmin(admin.ModelAdmin):
    ordering = ('id',)
    search_fields = ('categorie',)
    list_display = ('categorie', 'dateCreation',)
    fieldsets = (
    # Fieldset 1 : meta-info 
   ('Général', {
       'description': 'Renseignez ici les différentes catégories que vous souhaitez voir abordées dans les mentions légales',
        'fields': ('categorie', 'contenu')
    }),
)

#_________________________________________________________________
# ABOUT 
#_________________________________________________________________
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('titre', 'dateCreation',)
    fieldsets = (
    # Fieldset 1 : meta-info 
   ('Général', {
       'description': 'Attention, cette page est unique. Si une section About existe déjà, n\'essayez pas d\'en sauvegarder une seconde, une erreur sera levée.',
        'fields': ('titre', 'contenu',)
    }),
    # Fieldset 2 : photo illustration de la section
    ('Photo de la section', {
       'fields': ('photo', )
    }),
)

#_________________________________________________________________
# DATA POLICY 
#_________________________________________________________________
@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    ordering = ('id',)
    search_fields = ('categorie',)
    list_display = ('categorie', 'dateCreation',)
    fieldsets = (
    # Fieldset 1 : meta-info 
   ('Général', {
       'description': 'Renseignez ici les différentes catégories que vous souhaitez voir abordées dans la politique de confidentialité des données',
        'fields': ('categorie', 'contenu')
    }),
)