from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.login, name="login"),
    path("register-user/", views.register_user, name="register-user"),
    path("user/", views.login, name="user"),
    path("add-books/", views.add_books, name="add-books"),
    path("book-detail/<int:id>/", views.book_detail, name="book-detail"),
]
