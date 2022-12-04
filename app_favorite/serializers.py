from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from app_favorite.models import Favorite, TimeMovies


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(required=False)
    class Meta:
        model = Favorite
        fields = "__all__"

    def get_user(self,obj):
        return obj.user.username

    def create(self,validated_data):
        request = self.context['request']
        obj = self.Meta.model(**validated_data)
        obj.user = request.user
        obj.save()
        return obj

class TimeMoviesSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(required=False)
    class Meta:
        model = TimeMovies
        fields = "__all__"

    def get_user(self,obj):
        return obj.user.username

    def create(self,validated_data):
        request = self.context['request']
        obj = self.Meta.model(**validated_data)
        obj.user = request.user
        obj.save()
        return obj

    def update(self,instance,validated_data):
        request = self.context['request']
        instance.time = request.data.get('time')
        instance.chap = request.data.get('chap')
        instance.save()
        return instance