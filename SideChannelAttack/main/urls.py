from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.index, name="homepage"),
    path('home/',views.home, name="homepage"),
    path('about/',views.about, name="about"),
    path('guide/',views.guide, name="guide"),
    path('tools/',views.tools, name="tools"),
    path('tools/upload',views.upload,name='upload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)