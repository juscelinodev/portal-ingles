from unittest.util import _MAX_LENGTH
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.utils.timezone import now

from django.contrib.auth.models import AbstractUser

from portal.managers import UserManager

# Create your models here.

class Usuario(AbstractUser):
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    objects = UserManager()


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.nome_categoria

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome_categoria)
        super(Categoria, self).save(*args, **kwargs)


class Curso(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    nome_curso = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique=True, primary_key=True, auto_created=False)
    slug = models.SlugField(max_length=200, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.TextField(blank=False)
    thumbnail = models.ImageField(upload_to='thumbnails/',null=True, blank=True)
    # video_url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_curso

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome_curso)
        super(Curso, self).save(*args, **kwargs)


class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='aulas')
    nome_aula = models.CharField(max_length=100)
    video_url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_aula


class Matricula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='matriculas')
    data_matricula = models.DateTimeField(default=now)
    
