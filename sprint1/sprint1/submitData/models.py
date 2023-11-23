from django.db import models
from .resources import STATUS_CHOICES, LEVEL
from .services import get_path_upload_photos


class Users(models.Model):
    email = models.EmailField()
    fam = models.TextField(max_length=64, verbose_name='Фамилия')
    name = models.TextField(max_length=64, verbose_name='Имя')
    otc = models.TextField(max_length=64, verbose_name='Отчество')
    phone = models.TextField(max_length=64, verbose_name='Контактный телефон')

    def __str__(self):
        return f'{self.fam} {self.name} {self.email}'

    class Meta:
        verbose_name = "Турист"


class Coordinates(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}'

    class Meta:
        verbose_name = "Координаты"


class Levels(models.Model):
    winter = models.CharField(max_length=3, choices=LEVEL, verbose_name='Зима', null=True, blank=True)
    summer = models.CharField(max_length=3, choices=LEVEL, verbose_name='Лето', null=True, blank=True)
    autumn = models.CharField(max_length=3, choices=LEVEL, verbose_name='Осень', null=True, blank=True)
    spring = models.CharField(max_length=3, choices=LEVEL, verbose_name='Весна', null=True, blank=True)

    def __str__(self):
        return f"зима: {self.winter}, весна: {self.spring}, лето: {self.summer}, осень: {self.autumn}"

    class Meta:
        verbose_name = "Уровень сложности"


class Pereval(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE)
    beauty_title = models.TextField(blank=True, verbose_name='Основное название вершины', null=True)
    title = models.CharField(max_length=128, blank=True, null=True, verbose_name='Название вершины')
    other_titles = models.CharField(max_length=128, blank=True, null=True, verbose_name='Другое название')
    connect = models.CharField(max_length=255, blank=True, verbose_name='Связывает', null=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    def __str__(self):
        return f'{self.pk} {self.add_time} {self.beauty_title}'


class Images(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    data = models.ImageField(upload_to=get_path_upload_photos, verbose_name='Изображение')
    title = models.TextField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f'{self.pk} {self.data}'
