# Generated by Django 4.2.6 on 2023-11-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='email'),
        ),
    ]
