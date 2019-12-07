from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from stories.models import Story, Img
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Here a view that needs to treat a list of stories.
It needs a Paginator to define how many articles we want to display per page
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@cache_page(60 * 360)
def storiesMain(request):
    list_stories = Story.objects.all()

    paginator = Paginator(list_stories, 2)
    page = request.GET.get('page')
    stories = paginator.get_page(page)

    return render(request, 'stories/storiesMain.html', {'list_stories': stories})


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Here a view for one specific story, the primary key (id) is used to identify the good one.
If that story does not exist, a 404 error is sent.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@cache_page(60 * 360)
def storiesDetails(request, id): 
    story = get_object_or_404(Story, id=id)
    images = Img.objects.all().filter(story = story)
    return render(request, 'stories/storiesDetails.html', {'story': story, 'images': images})