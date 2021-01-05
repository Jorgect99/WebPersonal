from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length = 120, verbose_name = "Nombre")
    img = models.ImageField(upload_to = "skills" ,verbose_name = "Imagen")
    level = models.SmallIntegerField(verbose_name="Order", default = 0)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edicion")

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'
        ordering = ['level']

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length = 120, verbose_name = "Nombre")
    content = RichTextField(verbose_name = "Descripcion")
    img = models.ImageField(upload_to = "about" ,verbose_name = "Imagen")
    skills = models.ManyToManyField(Skill, verbose_name = "Skills")

    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edicion")

    class Meta:
        verbose_name = 'about'
        ordering = ["-created"]

    def __str__(self):
        return self.name

