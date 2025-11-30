from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Book
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    books = Book.objects.all()
    return render(request, "books/home.html", {"books": books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/book_detail.html", {"book": book})

@login_required
def add_book(request):
    # validate form submission and save book to database
    if request.method == "POST":
        form = BookForm(request.POST)
        # render errors
        if form.is_valid():
            book = form.save(commit=False)
            book.posted_by = str(request.user)
            book.save()
            return redirect("/", book_id=book.id)
        return render(request, "books/add_book.html", {"form": form})
    # display empty form
    return render(request, "books/add_book.html", {"form": BookForm()})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:book_detail", book_id=book.id)

    form = BookForm(instance=book)
    return render(request, "books/edit_book.html", {"form": form, "book": book})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("books:home")

    return render(request, "books/delete_book.html", {"book": book})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("books:home")
    form = UserCreationForm()
    return render(request, "books/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("books:home")
    form = AuthenticationForm()
    return render(request, "books/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("books:home")
