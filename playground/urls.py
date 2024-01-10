from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^movie$',views.MovieApi),
    url(r'^movie$',views.MovieApi),
    url(r'^movie/([0-9]+)$',views.MovieApi),
    path('admin/', admin.site.urls),
]
