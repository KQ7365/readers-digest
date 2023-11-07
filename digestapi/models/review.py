from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review')
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='book_review')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.CharField(max_length=155)
    date = models.DateField(auto_now_add=True)