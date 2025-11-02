from django.contrib import admin

from .models import Book, Student, Borrow, Author, Subject

# Register your models here.

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrow)
admin.site.register(Author)
admin.site.register(Subject)
