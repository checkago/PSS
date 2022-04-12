from datetime import date
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Псевдоним')
    date = models.DateTimeField(default=date.today, verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='news', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости сайта'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория')
    image = models.ImageField(upload_to='gallery', verbose_name='Фото')



