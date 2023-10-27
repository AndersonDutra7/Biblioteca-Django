from django.contrib import admin
from .models import Books, Genders


class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'in_stock']
    list_filter = ['in_stock']
    search_fields = ['name']


admin.site.register(Books, BooksAdmin)

admin.site.register(Genders)