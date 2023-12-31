# Generated by Django 4.2.7 on 2023-11-23 13:54

from django.db import migrations, models
import django.db.models.deletion
import submitData.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
            options={
                'verbose_name': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, choices=[('-', '-'), ('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('3b+', '3Б+')], max_length=3, null=True, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, choices=[('-', '-'), ('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('3b+', '3Б+')], max_length=3, null=True, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, choices=[('-', '-'), ('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('3b+', '3Б+')], max_length=3, null=True, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, choices=[('-', '-'), ('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('3b+', '3Б+')], max_length=3, null=True, verbose_name='Весна')),
            ],
            options={
                'verbose_name': 'Уровень сложности',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fam', models.TextField(max_length=255, verbose_name='Фамилия')),
                ('name', models.TextField(max_length=255, verbose_name='Имя')),
                ('otc', models.TextField(max_length=255, verbose_name='Отчество')),
                ('phone', models.TextField(max_length=255, verbose_name='Контактный телефон')),
            ],
            options={
                'verbose_name': 'Турист',
            },
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('beauty_title', models.TextField(blank=True, null=True, verbose_name='Основное название вершины')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Название вершины')),
                ('other_titles', models.CharField(blank=True, max_length=128, null=True, verbose_name='Другое название')),
                ('connect', models.CharField(blank=True, max_length=255, null=True, verbose_name='Связывает')),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'в работе'), ('accepted', 'принят'), ('rejected', 'отклонен')], default='new', max_length=16)),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submitData.coordinates')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submitData.levels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submitData.users')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(upload_to=submitData.services.get_path_upload_photos, verbose_name='Изображение')),
                ('title', models.TextField(blank=True, max_length=64, null=True)),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='submitData.pereval')),
            ],
        ),
    ]
