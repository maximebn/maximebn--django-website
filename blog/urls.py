from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogList, name='blogList'),
    path('category/<categorie>', views.blogListByCategory, name='blogListByCategory'),
    path('blogDetails/<int:id>-<slug:slug>', views.blogDetails, name='blogDetails')
]

