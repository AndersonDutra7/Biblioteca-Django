from django.shortcuts import render, redirect
from .models import Books, Genders, Reservations, Loans
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import BookForm


def index(request):
    books = Books.objects.all().order_by("cod")

    for book in books:
        print(f"book.name + book.gender")
    return render(request, "pages/index.html", {"books": books})


def index_list(request):
    books = Books.objects.all().order_by("cod")
    return render(request, "pages/index_list.html", {"books": books})


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

        last_book = Books.objects.order_by("-cod").first()
        if last_book:
            cod = last_book.cod + 1
        else:
            cod = 1

        gender = request.POST["gender"]
        book_cover = request.FILES.get("book_cover")
        author = request.POST["author"]
        description = request.POST.get("description")

        pages = request.POST["pages"]
        qtd = request.POST["qtd"]

        if (
            not name
            or not gender
            or not book_cover
            or not author
            or not pages
            or not qtd
        ):
            messages.error(request, "Por favor, preencha todos os campos.")
            return redirect("add-books")

        try:
            pages = int(pages)
            qtd = int(qtd)
        except ValueError:
            messages.error(
                request, "As páginas e a quantidade devem ser números inteiros."
            )
            return redirect("add-books")

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

        messages.success(request, "Livro adicionado com sucesso!")
        # genders = Genders.objects.all()
        # return render(request, "pages/add_books.html", {"genders": genders})
        messages.success(request, "Livro adicionado com sucesso!")
        return redirect("add-books")
    else:
        genders = Genders.objects.all()
        return render(request, "pages/add_books.html", {"genders": genders})


def book_detail(request, id):
    book = Books.objects.get(id=id)
    return render(request, "pages/book_detail.html", {"book": book})


def delete_book(request, id):
    book = Books.objects.get(id=id).delete()
    return redirect("home")


def edit_book(request, id):
    book = Books.objects.get(id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Livro atualizado com sucesso.")
            return redirect("book-detail", id=id)
        else:
            messages.error(request, "Por favor, corrija os erros no formulário.")
    else:
        form = BookForm(instance=book)

    return render(request, "pages/edit_book.html", {"form": form, "book": book})


# def loan_book(request, id):
#     book = Books.objects.get(id=id)
#     if int(book.qtd) == 0:
#         book.in_stock = False
#         book.save()
#         messages.success(request, "Este livro não possui estoque!")
#     else:
#         book.qtd -= 1
#         book.save()
#         messages.success(request, "Empréstimo realizado com sucesso!")
#     return redirect("book-detail", id=id)


def return_book(request, id):
    book = Books.objects.get(id=id)
    loan = Loans.objects.filter(book=book).first()

    if loan:
        book.qtd += 1
        book.in_stock = True
        book.save()
        loan.delete()
        messages.success(request, "Devolução realizada com sucesso!")
    else:
        messages.warning(request, "Não há empréstimo para o livro.")

    return redirect("book-detail", id=id)


def back(request):
    return redirect("home")


@login_required
def reserve_book(request, id):
    book = Books.objects.get(id=id)
    user = request.user

    if book.in_stock:
        reservation = Reservations.objects.create(book=book, user=user)
        messages.success(request, f"O livro {book.name} foi reservado com sucesso!")
    else:
        messages.warning(
            request, f"O livro {book.name} não está disponível para reserva."
        )

    return redirect("book-detail", id=id)


@login_required
def lend_book(request, id):
    book = Books.objects.get(id=id)
    reservations = Reservations.objects.filter(book=book)

    if request.method == "POST":
        selected_user_id = request.POST.get("selected_user")

        if selected_user_id:
            selected_user = get_object_or_404(User, id=selected_user_id)

            # Lógica para criar um empréstimo
            loan = Loans.objects.create(book=book, user=selected_user)

            # Atualizar a quantidade de livros
            book.qtd -= 1
            if book.qtd == 0:
                book.in_stock = False
            else:
                book.in_stock = True
            book.save()

            # Excluir a reserva
            reservation = Reservations.objects.filter(
                book=book, user=selected_user
            ).first()
            if reservation:
                reservation.delete()

            messages.success(
                request,
                f"Empréstimo realizado para {selected_user.name} com sucesso!",
            )

        else:
            messages.error(
                request,
                f"Falha ao emprestar! O livro {book.name} não possui estoque.!",
            )

    return render(
        request, "pages/lend_book.html", {"book": book, "reservations": reservations}
    )


@login_required
def view_loans(request):
    loans = Loans.objects.all()
    return render(request, "pages/view_loans.html", {"loans": loans})
