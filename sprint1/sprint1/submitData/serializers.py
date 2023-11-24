from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


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
    class Meta:
        model = Images
        fields = ['pereval', 'data', 'title', ]


class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coordinates = CoordinatesSerializer()
    level = LevelsSerializer(allow_null=True)
    images = ImagesSerializer(many=True)# убрать для корректного добавления перевала, а затем изображения через HTML

    class Meta:
        model = Pereval
        fields = (
            'add_time', 'beauty_title', 'title', 'other_titles', 'connect', 'user', 'coordinates', 'level', 'images')# убрать 'images' для корректного добавления перевала, а затем изображения через HTML
        read_only_fields = ['status']

    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coordinates = validated_data.pop('coordinates')
        level = validated_data.pop('level')
        images = validated_data.pop('images')# убрать для корректного добавления перевала, а затем изображения через HTML


        pick_user = Users.objects.filter(email=user['email'])
        if pick_user.exists():
            users_serializer = UsersSerializer(data=user)
            users_serializer.is_valid(raise_exception=True)
            user = users_serializer.save()
        else:
            user = Users.objects.create(**user)

        coordinates = Coordinates.objects.create(**coordinates)
        level = Levels.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coordinates=coordinates, level=level, status='new')

        for image in images:# убрать для корректного добавления перевала, а затем изображения через HTML
            data = image('data')# убрать для корректного добавления перевала, а затем изображения через HTML
            title = image('title')# убрать для корректного добавления перевала, а затем изображения через HTML
            Images.objects.create(pereval=pereval, data=data, title=title)# убрать для корректного добавления перевала, а затем изображения через HTML

        return pereval
