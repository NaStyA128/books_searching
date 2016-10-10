from django.contrib import admin
from .models import Book, Page

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_book', 'author',
                    'quantity_pages', 'description']


class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'page_number',
                    'text', 'part', 'section', 'chapter']


admin.site.register(Book, BookAdmin)
admin.site.register(Page, PageAdmin)
