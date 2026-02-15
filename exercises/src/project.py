import json
import os
from datetime import datetime


# =============================================================================
# PART 1: HELPER FUNCTIONS
# =============================================================================

def format_date(dt: datetime = None) -> str:
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d")


def generate_id(prefix: str, existing_ids: list) -> str:
    if not existing_ids:
        return f"{prefix}_0001"
    numbers = [
        int(i.split("_")[1]) for i in existing_ids if i.startswith(prefix + "_")
    ]
    next_num = max(numbers) + 1 if numbers else 1
    return f"{prefix}_{next_num:04d}"


def search_items(items: list, **criteria) -> list:
    results = []
    for item in items:
        match = True
        for key, value in criteria.items():
            if key not in item:
                match = False
                break
            item_val = item[key]
            if isinstance(item_val, str) and isinstance(value, str):
                if item_val.lower() != value.lower():
                    match = False
                    break
            else:
                if item_val != value:
                    match = False
                    break
        if match:
            results.append(item)
    return results


# =============================================================================
# PART 2: BOOK CLASS
# =============================================================================

class Book:
    GENRES = ["Fiction", "Non-Fiction", "Science", "History", "Technology"]

    def __init__(self, book_id: str, title: str, author: str, genre: str, available: bool = True):
        if genre not in Book.GENRES:
            raise ValueError(f"Invalid genre: {genre}")
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def to_dict(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["genre"],
            data.get("available", True)
        )

    def __str__(self) -> str:
        status = "Available" if self.available else "Checked Out"
        return f"[{self.book_id}] {self.title} by {self.author} ({self.genre}) - {status}"


# =============================================================================
# PART 3: BORROWER CLASS
# =============================================================================

class Borrower:
    MAX_BOOKS = 3

    def __init__(self, borrower_id: str, name: str, email: str, borrowed_books: list = None):
        self.borrower_id = borrower_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books if borrowed_books else []

    def can_borrow(self) -> bool:
        return len(self.borrowed_books) < Borrower.MAX_BOOKS

    def borrow_book(self, book_id: str) -> bool:
        if not self.can_borrow():
            return False
        self.borrowed_books.append(book_id)
        return True

    def return_book(self, book_id: str) -> bool:
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def to_dict(self) -> dict:
        return {
            "borrower_id": self.borrower_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Borrower":
        return cls(
            data["borrower_id"],
            data["name"],
            data["email"],
            data.get("borrowed_books", [])
        )


# =============================================================================
# PART 4: LIBRARY CLASS (Main System)
# =============================================================================

class Library:
    def __init__(self, name: str, data_dir: str = "."):
        self.name = name
        self.books = {}
        self.borrowers = {}
        self.books_file = os.path.join(data_dir, "library_books.json")
        self.borrowers_file = os.path.join(data_dir, "library_borrowers.json")
        self.load()

    def load(self) -> None:
        try:
            with open(self.books_file, "r", encoding="utf-8") as f:
                books_data = json.load(f)
                self.books = {b["book_id"]: Book.from_dict(b) for b in books_data}
        except FileNotFoundError:
            self.books = {}
        try:
            with open(self.borrowers_file, "r", encoding="utf-8") as f:
                borrowers_data = json.load(f)
                self.borrowers = {br["borrower_id"]: Borrower.from_dict(br) for br in borrowers_data}
        except FileNotFoundError:
            self.borrowers = {}

    def save(self) -> None:
        with open(self.books_file, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books.values()], f, indent=2)
        with open(self.borrowers_file, "w", encoding="utf-8") as f:
            json.dump([br.to_dict() for br in self.borrowers.values()], f, indent=2)

    def add_book(self, title: str, author: str, genre: str) -> Book:
        new_id = generate_id("BOOK", list(self.books.keys()))
        book = Book(new_id, title, author, genre)
        self.books[new_id] = book
        self.save()
        return book

    def add_borrower(self, name: str, email: str) -> Borrower:
        new_id = generate_id("USER", list(self.borrowers.keys()))
        borrower = Borrower(new_id, name, email)
        self.borrowers[new_id] = borrower
        self.save()
        return borrower

    def checkout_book(self, book_id: str, borrower_id: str) -> bool:
        if book_id not in self.books or borrower_id not in self.borrowers:
            return False
        book = self.books[book_id]
        borrower = self.borrowers[borrower_id]
        if not book.available or not borrower.can_borrow():
            return False
        book.available = False
        borrower.borrow_book(book_id)
        self.save()
        return True

    def return_book(self, book_id: str, borrower_id: str) -> bool:
        if book_id not in self.books or borrower_id not in self.borrowers:
            return False
        book = self.books[book_id]
        borrower = self.borrowers[borrower_id]
        if book_id not in borrower.borrowed_books:
            return False
        book.available = True
        borrower.return_book(book_id)
        self.save()
        return True

    def search_books(self, **criteria) -> list:
        books_data = [b.to_dict() for b in self.books.values()]
        return search_items(books_data, **criteria)

    def get_available_books(self) -> list:
        return [b for b in self.books.values() if b.available]

    def get_borrower_books(self, borrower_id: str) -> list:
        if borrower_id not in self.borrowers:
            return []
        borrower = self.borrowers[borrower_id]
        return [self.books[bid] for bid in borrower.borrowed_books if bid in self.books]

    def get_statistics(self) -> dict:
        total_books = len(self.books)
        available_books = sum(1 for b in self.books.values() if b.available)
        checked_out = total_books - available_books
        total_borrowers = len(self.borrowers)
        books_by_genre = {genre: 0 for genre in Book.GENRES}
        for b in self.books.values():
            books_by_genre[b.genre] = books_by_genre.get(b.genre, 0) + 1
        return {
            "total_books": total_books,
            "available_books": available_books,
            "checked_out": checked_out,
            "total_borrowers": total_borrowers,
            "books_by_genre": books_by_genre
        }