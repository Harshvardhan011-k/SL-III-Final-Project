from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def home(request):
    books = Book.objects.all()
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'books/home.html', {'books': books, 'form': form})
