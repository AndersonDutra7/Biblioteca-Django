from django.db import models

class Genders(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

class Books(models.Model):
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
        verbose_name = 'Book'
        verbose_name_plural = 'Books'