from django.db import models

# Create your models here.


class Book(models.Model):
    name_book = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quantity_pages = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name_book


class Page(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    page_number = models.PositiveIntegerField()
    text = models.TextField()
    part = models.CharField(max_length=100, null=True, blank=True)
    section = models.CharField(max_length=100, null=True, blank=True)
    chapter = models.CharField(max_length=100, null=True, blank=True)
