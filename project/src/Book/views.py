from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
# Create your views here.

def One_Book(request, Book_id):
    #OneBook = Book.objects.get(pk=Book_id)
    OneBook = get_object_or_404(Book, pk=Book_id)
    print(OneBook.name_Book)

    content = {'Name': OneBook.name_Book,
     'Image': OneBook.Image,
     'pages': OneBook.pages,
     'active':OneBook.active,}

    return render(request, 'Book/Book.html', {'content': content})

def All_Books(request):
    return render(request, 'Book/Books.html', {'Books':  Book.objects.all()})