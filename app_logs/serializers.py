from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    # avatar = serializers.SerializerMethodField()

    # def get_avatar(self, user):
    #     request = self.context['request']
    #     if user.avatar:
    #         name = user.avatar.name
    #         if name.startswith("media/"):
    #             path = '/%s' % name
    #         else:
    #             path = '/media/%s' % name
    #         return request.build_absolute_uri(path)
    #     else:
    #         return request.build_absolute_uri('/media/avatar-mac-dinh.png')

    def create(self, validated_data):
        # request = self.context['request']
        user = User(**validated_data)
        # user.avatar = request.data.get('avatar')
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name",
                  "username", "password", "date_joined"]
        extra_kwargs = {
            'password': {'write_only': 'true'},
            'date_joined': {'read_only': 'true'}
        }
