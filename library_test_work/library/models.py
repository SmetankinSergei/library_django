from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    isbn = models.CharField(max_length=30, unique=True)


class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    reg_date = models.DateTimeField(auto_now_add=True)
