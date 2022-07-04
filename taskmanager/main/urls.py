from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about-us'),
    path('create', views.create, name='create'),
]
