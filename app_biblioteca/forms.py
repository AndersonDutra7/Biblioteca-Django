from django import forms
from .models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            "cod",
            "name",
            "gender",
            "book_cover",
            "author",
            "pages",
            "qtd",
            "in_stock",
        ]
