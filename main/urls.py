from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home_url"),
    path('birja-url', birja, name="birja_url"),
    path('profil-url', birja, name="profil_url"),


]