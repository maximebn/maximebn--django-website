from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from stories.models import Story, Img

@cache_page(60 * 360)
def storiesMain(request):
    list_stories = Story.objects.all()

    return render(request, 'stories/storiesMain.html', {'list_stories': list_stories})


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Here a view for one specific story, the primary key (id) is used to identify the good one.
If that story does not exist, a 404 error is sent.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@cache_page(60 * 360)
def storiesDetails(request, id): 
    story = get_object_or_404(Story, id=id)
    images = Img.objects.all().filter(story = story)
    return render(request, 'stories/storiesDetails.html', {'story': story, 'images': images})