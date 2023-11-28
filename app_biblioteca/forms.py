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

        widgets = {
            "cod": forms.TextInput(attrs={"class": "input-field"}),
            "name": forms.TextInput(attrs={"class": "input-field"}),
            "gender": forms.TextInput(attrs={"class": "input-field"}),
            "book_cover": forms.FileInput(attrs={"class": "file-input"}),
            "author": forms.TextInput(attrs={"class": "input-field"}),
            "pages": forms.NumberInput(attrs={"class": "input-field"}),
            "qtd": forms.NumberInput(attrs={"class": "input-field"}),
            "in_stock": forms.CheckboxInput(attrs={"class": "checkbox-input"}),
        }
