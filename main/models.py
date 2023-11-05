from django.db import models

# Create your models here.
# Поле не обязательно для заполнения
NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    """Клас для создания модели"""
    first_nami = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)

    email = models.CharField(max_length=150, unique=True, **NULLABLE, help_text='введите email учебного заведения',
                             verbose_name='email')

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        """Обязательно делает строковое отображение"""
        return f'{self.first_nami} {self.last_name}'

    class Meta:
        """Описание"""
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)  # для сортировки


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='студент')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
