from django.contrib import admin

from .models import Author, Category, Editorial, Book

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Editorial)
admin.site.register(Book)

