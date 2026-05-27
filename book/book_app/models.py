from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    book_des=models.CharField(max_length=100)
    book_type = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()
