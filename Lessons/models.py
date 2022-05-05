from datetime import datetime
from django.contrib.auth.models import User as VisitOf
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField 


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    url = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    about = models.TextField(verbose_name='О себе')
    image = models.ImageField(upload_to='students/%Y/%m/%d/', verbose_name='Изображение')
    url = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Direction(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    url = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='course/%Y/%m/%d/', verbose_name='фото')
    year = models.DateField(auto_now=False)
    country = CountryField()
    director = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='director', verbose_name='директор')
    students = models.ManyToManyField(User, verbose_name='студенты')
    Directions = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='direction')
    presentation = models.DateField(auto_now=False,
                                      default=datetime.today().strftime('%Y-%m-%d'),
                                      verbose_name='презентация')
    course_fees = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='стоимость курсов')
    # fees_on_country = models.PositiveIntegerField(verbose_name='Сборы в городах')
    # fees_on_world = models.PositiveIntegerField(verbose_name='Сборы по миру')
    slug = models.SlugField(unique=True, max_length=100)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title
        super(Course, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-year']
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class VideoLessons(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='video_lessons')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    video = models.ImageField(upload_to='video_lessons', verbose_name='видео')

    def __str__(self):
        return self.course

    class Meta:
        verbose_name_plural = 'видео уроки'


