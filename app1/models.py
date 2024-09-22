from django.db import models

# Create your models here.
class Book(models.Model):
     book_name = models.CharField(max_length=200)
     author_name = models.CharField(max_length=200)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     publication=models.CharField(max_length=200,null=True)
    
     def __str__(self):
        return self.book_name

class Student(models.Model):
    roll_num=models.IntegerField()
    stud_name = models.CharField(max_length=200)
    stud_class = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)

    def __str__(self):
        return self.stud_name
    
    
    

