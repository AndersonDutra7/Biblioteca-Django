from django.shortcuts import render, redirect
from .models import Books, Genders
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404


def index(request):
    books = Books.objects.all().order_by("cod")

    for book in books:
        print(f"book.name + book.gender")
    return render(request, "pages/index.html", {"books": books})


def stockless(request):
    books = Books.objects.filter(in_stock=False)
    return render(request, "pages/index.html", {"books": books})


def search_book(request):
    q = request.GET.get("q")
    books = Books.objects.all()
    if q:
        books = books.filter(name__icontains=q).order_by("cod")
    print(books)
    return render(request, "pages/index.html", {"books": books})


def add_books(request):
    if request.method == "POST":
        name = request.POST.get("name")

        unique_cod = False
        while not unique_cod:
            cod = randint(100, 10000)
            if not Books.objects.filter(cod=cod).exists():
                unique_cod = True

        gender = request.POST["gender"]
        book_cover = request.FILES.get("book_cover")
        author = request.POST["author"]
        description = request.POST.get("description")
        pages = request.POST["pages"]
        qtd = request.POST["qtd"]

        in_stock = True
        if int(qtd) == 0:
            in_stock = False

        Books.objects.create(
            user_id=request.user.id,
            cod=cod,
            name=name,
            gender_id=gender,
            book_cover=book_cover,
            author=author,
            description=description,
            pages=pages,
            qtd=qtd,
            in_stock=in_stock,
        )

        return redirect("home")
    else:
        genders = Genders.objects.all()
        return render(request, "pages/add_books.html", {"genders": genders})


def book_detail(request, id):
    book = Books.objects.get(id=id)
    return render(request, "pages/book_detail.html", {"book": book})


def delete_book(request, id):
    book = Books.objects.get(id=id).delete()
    return redirect("home")


# Importe as bibliotecas e os modelos necessários
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from .models import Books


def sell_book(request, book_id):
    book = Books.objects.get(id=book_id)

    if book.in_stock:
        if int(book.qtd) > 0:
            book.qtd -= 1
            book.save()

            if int(book.qtd) == 0:
                book.in_stock = False
                book.save()

            messages.success(request, "Livro reservado com sucesso!")
        else:
            messages.error(request, "Não há mais estoque disponível para este livro.")
    else:
        messages.error(
            request, "Este livro não está disponível para reserva no momento."
        )

    return redirect("book-detail", id=book_id)


def back(request):
    return redirect("home")
