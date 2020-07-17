from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


# Create your models here.

class Counters(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    hot_water_big = models.FloatField(null=True, blank=True, verbose_name='Горячая вода (Ванна)')
    hot_water_small = models.FloatField(null=True, blank=True, verbose_name='Горячая вода (Туалет)')
    cold_water_big = models.FloatField(null=True, blank=True, verbose_name='Холодная вода (Ванна)')
    cold_water_small = models.FloatField(null=True, blank=True, verbose_name='Холодная вода (Туалет)')
    electricity = models.FloatField(null=True, blank=True, verbose_name='Электроэнергия')
    warm = models.FloatField(null=True, blank=True, verbose_name='Отопление')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    edited = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Отредактировано')
    comments = models.TextField(null=True, blank=True, verbose_name='Примечания')
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    # rubric = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Показания счетчиков'
        verbose_name = 'Показание счетчиков'
        ordering = ['-published', 'title']


# class Category(models.Model):
#     name = models.CharField(max_length=20, verbose_name='Категория')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = 'Категории'
#         verbose_name = 'Категория'
#         ordering = ['name']
