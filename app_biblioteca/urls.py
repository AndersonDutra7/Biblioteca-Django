from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("user/", views.login, name="user"),
    path("add-books/", views.add_books, name="add-books"),
    path("book-detail/<int:id>/", views.book_detail, name="book-detail"),
]
