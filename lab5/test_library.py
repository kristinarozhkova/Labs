import pytest
from library import Book, Library

@pytest.fixture
def book():
    return Book("1984", "George Orwell")

@pytest.fixture
def library(book):
    lib = Library()
    lib.add_book(book)
    return lib


# Tests for Book.borrow()
def test_borrow_book(book):
    book.borrow()
    assert book.is_borrowed is True

def test_borrow_already_borrowed(book):
    book.borrow()
    with pytest.raises(ValueError):
        book.borrow()


# Tests for Book.return_book()
def test_return_book(book):
    book.borrow()
    book.return_book()
    assert book.is_borrowed is False

def test_return_not_borrowed(book):
    with pytest.raises(ValueError):
        book.return_book()


# Tests for Library.available_books()
def test_available_books(library, book):
    assert book in library.available_books()

def test_book_not_available_when_borrowed(library, book):
    book.borrow()
    assert book not in library.available_books()
