import email
from datetime import date
from django.urls import reverse
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, db_index=True, verbose_name='Название')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='Псевдоним')
    date = models.DateField(default=date.today, verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='news', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости сайта'

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Подкатегория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='gallery', verbose_name='Фото')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

    def __str__(self):
        return self.category.name


class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=18, blank=True, verbose_name='Телефон')
    portfolio = models.URLField(blank=True, verbose_name='Ссылка на портфолио')
    profile = models.URLField(blank=True, verbose_name='Ссылка на соцсети')
    where = models.CharField(max_length=250, blank=True, verbose_name='Где вы о нас узнали?')
    resume = models.FileField(upload_to='resume', verbose_name='Резюме')
    letter = models.FileField(upload_to='letters', blank=True, verbose_name='Сопроводительное письмо')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме соискателей'

    def __str__(self):
        return format(self.name +' '+ self.lastname)


class Feedback(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=18, blank=True, verbose_name='Телефон')
    site = models.URLField(blank=True, verbose_name='Сайт')
    text = models.TextField(blank=True, verbose_name='Текст')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return format(self.name +' '+ self.email)


