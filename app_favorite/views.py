from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *
from .models import *


class FavoriteAPIView(viewsets.ViewSet, generics.ListAPIView, generics.DestroyAPIView, generics.UpdateAPIView,
                   generics.CreateAPIView, generics.RetrieveAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        favorites = Favorite.objects.filter(user=self.request.user)
        q = self.request.query_params.get('q')
        if q is not None:
            favorites = favorites.filter(slug = q)

            # courses = courses.filter(subject__icontains=q)
            # Neu la icontains thi khong phan biet hoa thuong
        return favorites

class TimeMoiveAPIView(viewsets.ViewSet,generics.CreateAPIView,generics.UpdateAPIView,generics.ListAPIView,generics.DestroyAPIView):
    serializer_class = TimeMoviesSerializer
    permissions_classes = [permissions.AllowAny]
    queryset = TimeMovies.objects.all()
    @action(methods=['get'], detail=False, url_path='movie')
    def get_time_movie(self,request):
        q = self.request.query_params.get('q')
        timeMovies,_ = TimeMovies.objects.get_or_create(user=self.request.user,slug=q)
        return Response(TimeMoviesSerializer(timeMovies).data)