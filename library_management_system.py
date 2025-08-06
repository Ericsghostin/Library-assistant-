"""
Library Management System
"""

import os
import json

class Book:
    def __init__(self, title, author, year, isbn, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = is_available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn,
            "is_available": self.is_available
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["author"],
            data["year"],
            data["isbn"],
            data["is_available"]
        )

def load_books(filename="library_records.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        data = json.load(f)
        return [Book.from_dict(book) for book in data]

def save_books(books, filename="library_records.txt"):
    with open(filename, "w") as f:
        json.dump([book.to_dict() for book in books], f, indent=4)

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter year published: ")
    isbn = input("Enter ISBN: ")
    books.append(Book(title, author, year, isbn))
    print("Book added successfully!")

def display_books(books):
    if not books:
        print("No books in the library.")
        return
    for i, book in enumerate(books, start=1):
        status = "Available" if book.is_available else "Not Available"
        print(f"{i}. {book.title} by {book.author} ({book.year}) - ISBN: {book.isbn} - {status}")

def search_books(books):
    keyword = input("Enter title or author to search: ").lower()
    results = [book for book in books if keyword in book.title.lower() or keyword in book.author.lower()]
    if not results:
        print("No books found.")
    else:
        for book in results:
            status = "Available" if book.is_available else "Not Available"
            print(f"{book.title} by {book.author} ({book.year}) - ISBN: {book.isbn} - {status}")

def borrow_book(books):
    isbn = input("Enter ISBN of the book to borrow: ")
    for book in books:
        if book.isbn == isbn:
            if book.is_available:
                book.is_available = False
                print("Book borrowed successfully!")
            else:
                print("Book is currently not available.")
            return
    print("Book not found.")

def return_book(books):
    isbn = input("Enter ISBN of the book to return: ")
    for book in books:
        if book.isbn == isbn:
            if not book.is_available:
                book.is_available = True
                print("Book returned successfully!")
            else:
                print("Book was not borrowed.")
            return
    print("Book not found.")

def main():
    books = load_books()
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_book(books)
        elif choice == "2":
            display_books(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            save_books(books)
            print("Goodbye! Library records saved.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
