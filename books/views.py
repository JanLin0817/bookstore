from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def home(request):
    books = Book.objects.all()
    return render(request, "books/home.html", {"books": books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/book_detail.html", {"book": book})


def add_book(request):
    # validate form submission and save book to database
    if request.method == "POST":
        form = BookForm(request.POST)
        # render errors
        if form.is_valid():
            book = form.save()
            return redirect("/", book_id=book.id)
        return render(request, "books/add_book.html", {"form": form})
    # display empty form
    return render(request, "books/add_book.html", {"form": BookForm()})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:book_detail", book_id=book.id)

    form = BookForm(instance=book)
    return render(request, "books/edit_book.html", {"form": form, "book": book})


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("books:home")

    return render(request, "books/delete_book.html", {"book": book})
