# Generated by Django 3.1.2 on 2021-01-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210104_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='skills',
            field=models.ManyToManyField(to='core.Skill', verbose_name='Skills'),
        ),
    ]