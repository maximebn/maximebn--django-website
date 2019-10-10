from django.shortcuts import render
from annexes.models import Mentions, About, Policy


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Here a view that treats the about section
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mentions(request):
    list_mentions = Mentions.objects.all()

    return render(request, 'annexes/mentions.html', {'mentions': list_mentions})

def about(request):
    try:
        about = About.objects.last()
    except About.DoesNotExist:
        about = None

    return render(request, 'annexes/about.html', {'about': about})

def policy(request):
    list_policy = Policy.objects.all()

    return render(request, 'annexes/policy.html', {'dataPolicies': list_policy})