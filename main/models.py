from django.db import models

# Create your models here.
# Поле не обязательно для заполнения
NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    """Клас для создания модели"""
    first_nami = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def  __str__(self):
        """Обязательно делает строковое отображение"""
        return f'{self.first_nami} {self.last_name}'

    class Meta:
        """Описание"""
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)        # для сортировки
