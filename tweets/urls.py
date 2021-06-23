from django.urls import path, include
from .views import home_view,tweet_detail_view

urlpatterns = [
    path("",home_view,name="home"),
    path("tweet/<int:tweet_id>",tweet_detail_view)
]