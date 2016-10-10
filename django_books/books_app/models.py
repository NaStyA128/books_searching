import logging
from django.db import models

# Create your models here.


FORMAT = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s ' \
         u'[%(asctime)s]  %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG,
                    filename=u'logs_django.log')


class BookManager(models.Manager):

    @staticmethod
    def book_id(id_book):
        logging.info('It get book with id {}.'.format(id_book))
        return Book.objects.get(id=id_book)


class PageManager(models.Manager):

    @staticmethod
    def search_text(text):
        logging.info('It get details about page with text: {}.'.format(text))
        return Page.objects.filter(text__icontains=text)


class Book(models.Model):
    name_book = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quantity_pages = models.PositiveIntegerField()
    description = models.TextField()
    objects = BookManager()

    def __str__(self):
        return self.name_book


class Page(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    page_number = models.PositiveIntegerField()
    text = models.TextField()
    part = models.CharField(max_length=100, null=True, blank=True)
    section = models.CharField(max_length=100, null=True, blank=True)
    chapter = models.CharField(max_length=100, null=True, blank=True)
    objects = PageManager()
