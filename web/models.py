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


class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Псевдоним')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title




