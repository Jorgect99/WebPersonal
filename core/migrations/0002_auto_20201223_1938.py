# Generated by Django 3.1.4 on 2020-12-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(upload_to='about', verbose_name='Imagen'),
        ),
    ]
