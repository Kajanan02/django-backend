from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.urls import re_path as url
from . import views
from . import authViews

urlpatterns = [
    url(r'^movie$',views.MovieApi),
    url(r'^movie$',views.MovieApi),
    url(r'^movie/([0-9]+)$',views.MovieApi),
    url(r'^contact$', views.ContactApi),
    url(r'^booking$', views.BookingApi),
    url(r'^faq$', views.FAQApi),
    url(r'^faq/([0-9]+)$', views.FAQApi),
    url(r'^rooms$', views.ROOMSApi),
    url(r'^login$', authViews.LoginApi),
    path('admin/', admin.site.urls),
]
