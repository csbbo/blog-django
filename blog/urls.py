from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('test/', views.test),
    path('article/',views.ArticleList.as_view()),
    path('tags/',views.TagList.as_view()),
    path('friend/',views.FriendList.as_view()),
    path('website/',views.WebSiteList.as_view()),
    path('feedback/',views.FeedBackList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
