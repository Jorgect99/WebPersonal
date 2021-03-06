# Generated by Django 3.1.4 on 2020-12-23 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201223_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('img', models.ImageField(upload_to='skills', verbose_name='Imagen')),
                ('level', models.SmallIntegerField(default=0, verbose_name='Order')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
                'ordering': ['level'],
            },
        ),
        migrations.AddField(
            model_name='about',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.skill'),
        ),
    ]
