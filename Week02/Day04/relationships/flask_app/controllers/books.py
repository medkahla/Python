from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.book import Book


@app.route('/books/new')
def new_book():
    users = User.get_all()
    books = Book.get_all()
    return render_template("new_book.html" , users = users, books=books)

@app.route('/books/create', methods=["POST"])
def create():
    Book.create_book(request.form)
    return redirect('/')
