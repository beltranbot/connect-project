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
        blank=False,
        default='',
        max_length=100,
    )
    subtitulo = models.CharField(
        blank=True,
        default='',
        max_length=100,
        null=True,
    )
    autores = models.ManyToManyField(
        Author,
        blank=True,
    )
    categorias = models.ManyToManyField(
        Category,
        blank=True,
    )
    fecha_publicacion = models.DateField(
        blank=True,
        null=True,
    )
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
    )
    imagen = models.ImageField(
        blank=True,
        default='./static/pic_folder/None/no-img.jpg',
        null=True,
        upload_to='./static/pic_folder/',
    )

    def __str__(self):
        return self.titulo
