from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('mentions/', views.mentions, name='mentions'),
    path('datapolicy/', views.policy, name='policy'),
    url('about/', views.about, name='about'),
]

