from django.contrib import admin
from .models import Books, Genders, Reservations, Loans


class BooksAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author", "in_stock"]
    list_filter = ["in_stock"]
    search_fields = ["name"]


admin.site.register(Books, BooksAdmin)
admin.site.register(Genders)
admin.site.register(Reservations)
admin.site.register(Loans)
