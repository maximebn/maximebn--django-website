from django.urls import path
from . import views

urlpatterns = [
    path('', views.storiesMain, name='storiesMain'),
    path('storiesDetails/<id>', views.storiesDetails, name='storiesDetails')
]