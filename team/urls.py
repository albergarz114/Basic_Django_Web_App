from django.urls import path
from .views import homePageView,aboutPageView,teamPageView,playerPageView

urlpatterns = [
    path("", homePageView, name= "home_page"),
    path("about/", aboutPageView, name = "about_page"),
    path("players/", teamPageView, name="players_page"),
    path("players/<int:player_id>/", playerPageView, name="player_data"),
]