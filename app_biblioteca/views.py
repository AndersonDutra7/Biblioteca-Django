from django.shortcuts import render, redirect
from .models import Books, Genders
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


def index(request):
    books = Books.objects.all().order_by("cod")

    for book in books:
        print(f"book.name + book.gender")
    return render(request, "pages/index.html", {"books": books})

    gender = models.ForeignKey(Genders, on_delete=models.CASCADE)
    book_cover = models.ImageField(blank=False)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()
    qtd = models.IntegerField()
    in_stock = models.BooleanField(default=False)


@login_required
def login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, "pages/login.html")
        else:
            return render(request, "pages/user.html")
    else:
        print("Usuário não cadastrado")


def register_user(request):
    return render(request, "pages/register_user.html")


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
