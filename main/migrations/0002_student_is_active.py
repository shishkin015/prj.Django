# Generated by Django 4.2.6 on 2023-10-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='учится'),
        ),
    ]
