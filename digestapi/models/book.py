from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_created')
    title = models.CharField(max_length=155)
    author = models.CharField(max_length=155)
    isbn = models.IntegerField()
    cover_image_url = models.CharField(max_length=200)
    categories = models.ManyToManyField(
        "Category",
        through='BookCategory',
        related_name="books"
    )