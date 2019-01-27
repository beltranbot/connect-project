from rest_framework import serializers
from .models import Author, Book, Category, Editorial


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'nombre'
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'titulo',
            'subtitulo',
            'autores',
            'categorias',
            'fecha_publicacion',
            'editorial',
            'descripcion',
            'imagen'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'nombre'
        )


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = (
            'id',
            'nombre'
        )
