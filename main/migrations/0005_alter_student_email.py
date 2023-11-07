# Generated by Django 4.2.6 on 2023-11-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, help_text='введите email учебного заведения', max_length=150, null=True, unique=True, verbose_name='email'),
        ),
    ]
