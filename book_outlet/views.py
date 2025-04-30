from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all()
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))['rating__avg']
    return render(request, "book_outlet/index.html", {'books': books,
                                                      'total_number_of_books':num_books,
                                                      'average_rating':int(avg_rating)})

def book_detail(request, slug):
    try:
        book = get_object_or_404(Book, slug=slug)
    except:
        raise Http404()
    
    return render(request, "book_outlet/book_detail.html", {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling,
    })

