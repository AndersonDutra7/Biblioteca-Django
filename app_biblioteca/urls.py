from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("add-books/", views.add_books, name="add-books"),
    path("book-detail/<int:id>/", views.book_detail, name="book-detail"),
    path("search-book/", views.search_book, name="search-book"),
    path("stockless/", views.stockless, name="stockless"),
    path("delete-book/<int:id>/", views.delete_book, name="delete-book"),
    path("loan-book/<int:id>/", views.loan_book, name="loan-book"),
    path("return-book/<int:id>/", views.return_book, name="return-book"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
