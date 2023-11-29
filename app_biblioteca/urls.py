from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("index_list/", views.index_list, name="index-list"),
    path("add-books/", views.add_books, name="add-books"),
    path("book-detail/<int:id>/", views.book_detail, name="book-detail"),
    path("search-book/", views.search_book, name="search-book"),
    path("stockless/", views.stockless, name="stockless"),
    path("delete-book/<int:id>/", views.delete_book, name="delete-book"),
    path("return-book/<int:id>/", views.return_book, name="return-book"),
    path("reserve-book/<int:id>/", views.reserve_book, name="reserve-book"),
    path("lend-book/<int:id>/", views.lend_book, name="lend-book"),
    path("view_loans/", views.view_loans, name="view-loans"),
    path("edit-book/<int:id>/", views.edit_book, name="edit-book"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
