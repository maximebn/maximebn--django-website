from django.contrib import admin
from annexes.models import Mentions, About, Policy
from django.conf import settings
from maximebn import staticAttributes


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
       'description': staticAttributes.ANNEXES_MENTIONS_DESC,
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
       'description': staticAttributes.ANNEXES_ABOUT_DESC,
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
       'description': staticAttributes.ANNEXES_DATA_DESC,
        'fields': ('categorie', 'contenu')
    }),
)