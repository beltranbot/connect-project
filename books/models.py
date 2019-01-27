from django.db import models

# Create your models here.


class Author(models.Model):
    nombre = models.CharField(
        max_length=100,
        blank=False,
        default=''
    )

    def __str__(self):
        return self.nombre


class Category(models.Model):
    nombre = models.CharField(
        max_length=100,
        blank=False,
        default=''
    )

    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(
        max_length=100,
        blank=False,
        default=''
    )

    def __str__(self):
        return self.nombre


class Book(models.Model):
    titulo = models.CharField(
        max_length=100,
        blank=False,
        default=''
    )
    subtitulo = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )
    autores = models.ManyToManyField(Author)
    categorias = models.ManyToManyField(Category)
    fecha_publicacion = models.DateField()
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE
    )
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
