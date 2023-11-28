from rest_framework import viewsets
from .serializers import UsersSerializer, CoordinatesSerializer, LevelsSerializer, ImagesSerializer, PerevalSerializer
from .models import Users, Coordinates, Levels, Images, Pereval


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordinatesViewSet(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer


class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Levels.objects.all()
    serializer_class = LevelsSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
   queryset = Pereval.objects.all()
   serializer_class = PerevalSerializer