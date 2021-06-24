from django.urls import path, include
from .views import home_view,tweet_detail_view,tweet_list_view,tweet_create_view

urlpatterns = [
    path("",home_view,name="home"),
    path("create-tweet",tweet_create_view,name="create"),
    path("tweet/<int:tweet_id>",tweet_detail_view),
    path("tweets",tweet_list_view)
]