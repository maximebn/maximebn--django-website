from django.contrib import admin
from .models import Img, Story

#_________________________________________________________________
# STORY 
#_________________________________________________________________

class ImgInline(admin.TabularInline):
    model = Img

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    inlines = [
        ImgInline,
    ]