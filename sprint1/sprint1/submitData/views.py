from rest_framework import viewsets
from .serializers import UsersSerializer, CoordinatesSerializer, LevelsSerializer, ImagesSerializer, PerevalSerializer, PerevalDetailSerializer
from .models import Users, Coordinates, Levels, Images, Pereval
from rest_framework import mixins, generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
#
#
# class CoordinatesViewSet(viewsets.ModelViewSet):
#     queryset = Coordinates.objects.all()
#     serializer_class = CoordinatesSerializer
#
#
# class LevelsViewSet(viewsets.ModelViewSet):
#     queryset = Levels.objects.all()
#     serializer_class = LevelsSerializer
#
#
# class ImagesViewSet(viewsets.ModelViewSet):
#     queryset = Images.objects.all()
#     serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class SubmitData(mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__email']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SubmitDetailData(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalDetailSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PerevalDetailSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Статус данных изменился на: {instance.status}. Редактирование запрещено')
            serializer.save()
            return Response({'state': 1, 'message': 'Данные успешно отредактированы'})
        return Response({'state': 0, 'message': serializer.errors})

