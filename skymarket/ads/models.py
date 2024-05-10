from django.db import models
from django.utils import timezone
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    """Создание модели объявления"""
    title = models.CharField(max_length=200, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор объявления', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    image = models.ImageField(upload_to="ads/", verbose_name="Изображение", **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']  # Фильтрация по дате создания


class Comment(models.Model):
    """Создание модели отзыва"""
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отзыва', **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']  # Фильтрация по дате создания
