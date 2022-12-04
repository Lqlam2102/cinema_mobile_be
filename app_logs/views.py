# from django.shortcuts import render
import re

from rest_framework.exceptions import Throttled
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, generics, status, permissions, views
from rest_framework.decorators import action, throttle_classes
from rest_framework.response import Response

from app_favorite.serializers import FavoriteSerializer
from .models import *
from .serializers import *

from django.conf import settings



# Create your views here.

class UserAPIView(viewsets.ViewSet, generics.CreateAPIView):
    # parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        # print(self.action)
        if self.action == 'get_current_user':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current-user')
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user, context={"request": request}).data,
                        status=status.HTTP_200_OK)
    @action(methods=['get'], detail=False, url_path='check-exist-user')
    def check_user_exist(self, request):
        # print(request.headers.get('username'))
        username = request.headers.get('username')
        if User.objects.filter(username=username):
            return Response(data='exist', status=status.HTTP_200_OK)
        else:
            return Response(data='not exist', status=status.HTTP_200_OK)

    # @action(methods=['get'], detail=False, url_path='favorites')
    # def get_my_favorites(self, request):
    #     data = request.user.favorite_set.all()
    #     return Response(FavoriteSerializer(data,many=True).data)
    # def perform_create(self, serializer):
    #     user = serializer.save()




class AuthInfoView(views.APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)
