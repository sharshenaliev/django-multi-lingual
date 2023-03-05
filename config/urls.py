"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from rest_framework import routers
from .yasg import urlpatterns as doc_urls

from apps.views.views_home import *
from apps.views.views_aboutus import OurTeam, Feedback
from apps.views.views_studyabroad import Countries, Category, Specialization, Languages, Photos, Centers

router = routers.SimpleRouter()
router.register(r'exams', ExamsViewset)


urlpatterns = [
    path('images', Images.as_view()),
    path('videos', Videos.as_view()),
    path('icons', Icons.as_view()),
    path('photos', Photos.as_view()),
    path('contacts', Contacts.as_view()),
    path('feedback', Feedback.as_view())
]

urlpatterns += doc_urls

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('components', Components.as_view()),
    path('advantages', Advantages.as_view()),
    path('ourteam', OurTeam.as_view()),
    path('countries', Countries.as_view()),
    path('category', Category.as_view()),
    path('specialization', Specialization.as_view()),
    path('languages', Languages.as_view()),
    path('centers', Centers.as_view()),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
