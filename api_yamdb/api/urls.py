from django.urls import include, path
from rest_framework import routers

from .views import (CategoryView, CommentViewSet, GenreView, ReviewViewSet,
                    TitleViewSet)

app_name = 'api'

v1 = routers.DefaultRouter()
v1.register('titles', TitleViewSet, basename='titles')
v1.register('categories', CategoryView, basename='categories')
v1.register('genres', GenreView, basename='genres')
v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(v1.urls)),
]
