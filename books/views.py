from django.shortcuts import render


class _Book:
    def __init__(self, id, title, author, year, rating, description=""):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating
        self.description = description

# mock data
BOOKS = [
    _Book(1, "Example Book", "Jane Doe", 2020, 4.5, "A great introduction to programming."),
    _Book(2, "Another Example", "John Smith", 2021, 4.8, "Advanced techniques for developers."),
    _Book(3, "Django for Beginners", "Alice Wang", 2023, 5.0, "Learn Django step by step."),
]


def home(request):
    return render(request, "books/home.html", {"books": BOOKS})


def book_detail(request, book_id):
    book = None
    for b in BOOKS:
        if b.id == book_id:
            book = b
            break

    return render(request, "books/book_detail.html", {"book": book})
