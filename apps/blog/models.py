from django.db import models
from ..account.models import User


# Create your models here.

class Food(models.Model):
    food_name = models.CharField('Название блюда', max_length=60)
    photo = models.FileField('Фото блюда', upload_to= 'media/')
    # ingredients = models.ForeignKey('Ingredients', on_delete=models.CASCADE,
    #                                 related_name='Состав блюда')
    description = models.CharField('Описание блюда', max_length=250)


    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name= 'author_comment')
    food = models.ForeignKey(Food,on_delete=models.CASCADE,related_name='food_comment')
    text = models.CharField('Комментарий', max_length=500)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)



class Category(models.Model):
    name = models.CharField('Название Категории', max_length=50)
    slug = models.SlugField(max_length=60)
    icon = models.ImageField(upload_to='media/category')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'author_post')
    title = models.CharField('название', max_length=150)
    text = models.TextField('текст поста')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)
    photo = models.ImageField('Фото блюда', upload_to='media/')
    is_draft = models.BooleanField('черновик', default=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



