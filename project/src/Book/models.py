from django.db import models
# Create your models here.

class Book(models.Model):
    name_Book = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=150, null=False)
    ISBN = models.CharField(max_length=25, null=False)
    Image = models.ImageField(upload_to = "photoes/%y/%m/%d", null=False)
    pages = models.CharField(max_length=10, null=False)
    description = models.TextField(null=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.ISBN

'''
class User (models.Model):

    select = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    firstname = models.CharField(max_length=25, null=False)
    lastname = models.CharField(max_length=25, null=False)
    gender = models.CharField(max_length=25, null=False, choices=select)
    date_of_login = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=50)
    book = models.ForeignKey(Book, related_name='my_book', on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname +' '+ self.lastname
'''