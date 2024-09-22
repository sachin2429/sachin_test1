from django.contrib import admin
from .models import Book,Student

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','book_name', 'author_name', 'price','publication')

@admin.register(Student)
class StudAdmin(admin.ModelAdmin):
    list_display = ('id','roll_num', 'stud_name', 'stud_class','mobile')




# Register your models here.
