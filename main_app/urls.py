from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/new/', views.ArtistCreate.as_view(), name="artist_create")
]
