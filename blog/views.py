from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import Article

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Here a view that needs to treat a list of articles.
It needs a Paginator to define how many articles we want to display per page
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@cache_page(60 * 10)
def blogList(request):
    list_articles = Article.objects.all()

    paginator = Paginator(list_articles, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'blog/blogList.html', {'list_articles': articles})


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Here a view that needs to treat one specific article, the primary key (id) is used to identify the good one.
If that article does not exist, a 404 error will be sent.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@cache_page(60 * 10)
def blogDetails(request, id, slug): 
    article = get_object_or_404(Article, id=id, slug=slug)
    last_articles = Article.objects.all().order_by('-date')[:3]

    return render(request, 'blog/blogDetails.html', {'article': article, 'last_articles': last_articles})


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Here a view that needs to treat a list of articles for one category.
Paginator is used again. Articles are simply filtered by category before being rendered.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@cache_page(60 * 10)
def blogListByCategory(request, categorie): 
    list_articles = Article.objects.filter(categorie__nom=categorie)

    paginator = Paginator(list_articles, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'blog/blogList.html', {'list_articles': articles})