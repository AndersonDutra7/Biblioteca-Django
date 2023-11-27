from django.db import models
from django.contrib.auth.models import User


class Genders(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "Gender"
        verbose_name_plural = "Genders"


class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    cod = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE)
    book_cover = models.ImageField(blank=False)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()
    qtd = models.IntegerField()
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Reservations(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reservou {self.book.name}"

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


class Loans(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} pegou emprestado {self.book.name}"

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
