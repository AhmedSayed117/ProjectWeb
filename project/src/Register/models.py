
from django.db import models
#from .. Book.models import Book
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class UsersName (models.Model):

    select = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    kind = [
        ('admin', 'admin'),
        ('user', 'user'),
    ]

    user =models.OneToOneField(User,on_delete=models.CASCADE)

    firstname = models.CharField(max_length=25, null=False)
    lastname = models.CharField(max_length=25, null=False)
    UserName = models.CharField(max_length=25, null=False, primary_key=True)
    gender = models.CharField(max_length=25, null=False, choices=select)
    date_of_login = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=50)
    kind = models.CharField(max_length=6, choices = kind)
    password = models.CharField(max_length=50)
    #book = models.ForeignKey(Book, related_name='my_book', on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + self.lastname
