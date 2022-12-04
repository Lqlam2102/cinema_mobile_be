from django.urls import path, include
from rest_framework import routers

from app_favorite.views import *
from .views import UserAPIView, AuthInfoView

routers = routers.DefaultRouter()
routers.register('users', UserAPIView, 'user')
routers.register('favorite', FavoriteAPIView, 'favorite')
routers.register('time', TimeMoiveAPIView, 'time')

urlpatterns = [
    path('', include(routers.urls)),
    path('oauth2-info/', AuthInfoView.as_view()),
]
