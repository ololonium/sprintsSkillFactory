from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['fam', 'name', 'otc', 'email', 'phone']


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude', 'height', ]


class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Levels
        fields = ['winter', 'summer', 'autumn', 'spring', ]


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()
    class Meta:
        model = Images
        fields = ['data', 'title', ]


class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coordinates = CoordinatesSerializer()
    level = LevelsSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = (
            'add_time', 'beauty_title', 'title', 'other_titles', 'connect', 'user', 'coordinates', 'level', 'images')


class PerevalDetailSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coordinates = CoordinatesSerializer()
    level = LevelsSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = (
            'add_time', 'beauty_title', 'title', 'other_titles', 'connect', 'user', 'coordinates', 'level', 'images')

    def validate(self, data):
        user_data = data.get('user')
        user = self.instance.user
        if user_data is not None:

            if user.name != user_data.get('name') \
                    or user.fam != user_data.get('fam') \
                    or user.otc != user_data.get('otc') \
                    or user.email != user_data.get('email') \
                    or user.phone != user_data.get('phone'):
                raise ValidationError({'message': 'Редактирование пользовательских данных запрещено'})
            return data