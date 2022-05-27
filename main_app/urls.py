from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name='about'),
    path('artists/', views.ArtistList.as_view(), name="artist_list")
    # <- here we have added the new path
]
