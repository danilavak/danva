from django.db import models
from  datetime import  date
class Category(models.Model):
    name=models.CharField('Название', max_length=30)
    description=models.TextField('Описание')
    url=models.SlugField(max_length=150, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
class Actor(models.Model):
    name=models.CharField('Имя',max_length=50)
    age=models.PositiveSmallIntegerField('Возраст', default=0)
    description=models.TextField('Описание')
    image=models.ImageField('Портрет', upload_to='actors/')
    def __str__(self):
        return  self.name
    class Meta:
        verbose_name = 'Актер или Режиссер'
        verbose_name_plural = 'Актеры или Режиссеры'
class Genre(models.Model):
    name=models.CharField('Название', max_length=30)
    description=models.TextField('Описание')
    url=models.SlugField(max_length=150, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'
class Films(models.Model):
    title=models.CharField('Название',max_length=60)
    description = models.TextField('Описание')
    tagline=models.CharField('Слоган',max_length=60)
    poster = models.ImageField('Постер', upload_to='movies/')
    year=models.PositiveSmallIntegerField('Год выпуска',max_length=4)
    country=models.CharField('Страна',max_length=40)
    directors=models.ManyToManyField(Actor,verbose_name='Режиссеры',related_name='Film_Director')
    actors=models.ManyToManyField(Actor,verbose_name='Актеры',related_name='Film_Actor')
    genres=models.ManyToManyField(Genre,verbose_name='Жанры',related_name='Genre')
    premiere=models.DateField('Дата премьеры',default=date.today)
    budget=models.PositiveSmallIntegerField('Бюджет', default=0)