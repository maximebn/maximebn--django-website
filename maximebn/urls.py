"""maximebn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('stories.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('other/', include('annexes.urls')),
    url('success/', TemplateView.as_view(template_name='success.html'), name="success"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# If Debug mode is on, I add a custom URL to test some specific custom pages (as error ones..)
if settings.DEBUG:
    urlpatterns += url('success/', TemplateView.as_view(template_name='success.html'), name="success"),
    urlpatterns += url('404/', TemplateView.as_view(template_name='404.html'), name="404"),