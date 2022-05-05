# Generated by Django 4.0.4 on 2022-05-05 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='course/%Y/%m/%d/', verbose_name='фото')),
                ('year', models.DateField()),
                ('presentation', models.DateField(default='2022-05-05', verbose_name='презентация')),
                ('course_fees', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='стоимость курсов')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.URLField(verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('about', models.TextField(verbose_name='О себе')),
                ('image', models.ImageField(upload_to='students/%Y/%m/%d/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_video_lesson', to='Lessons.course')),
                ('visits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Голоса',
            },
        ),
        migrations.CreateModel(
            name='VideoLessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('video', models.ImageField(upload_to='video_lessons', verbose_name='видео')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_lessons', to='Lessons.course')),
            ],
            options={
                'verbose_name_plural': 'видео уроки',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Lessons.review', verbose_name='Ответить')),
                ('video_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_video_lesson', to='Lessons.course')),
                ('visitOf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='Directions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direction', to='Lessons.direction'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='Lessons.category'),
        ),
        migrations.AddField(
            model_name='course',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='Lessons.user', verbose_name='директор'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='Lessons.user', verbose_name='студенты'),
        ),
    ]
