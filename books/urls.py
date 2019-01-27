from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('editorials/', views.EditorialList.as_view()),
    path('editorials/<int:pk>/', views.EditorialDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)