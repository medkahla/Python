from flask_app import app
from flask import request ,render_template, session, redirect, flash
# from flask_app.models.user import User
from flask_app.models.book import Book


@app.route('/books/new')
def adding_book():
    return render_template('books_add.html')

@app.route('/books/create', methods=["post"])
def create_book():
    print(request.form)
    if(Book.validate(request.form)):
        data = {
            **request.form,'user_id':session["user_id"]
        }
        Book.create_book(data)
        return redirect('/books')
    return redirect('/books/new')

@app.route('/books/<int:book_id>')
def show_book(book_id):
    if not 'user_id' in session:
        return redirect('/')
    
    book = Book.get_one_with_user(book_id)
    return render_template('books_show.html', book=book)

@app.route('/books/<int:book_id>/edit')
def edit_book(book_id):
    if not 'user_id' in session:
        return redirect('/')
    book = Book.get_by_id(book_id)
    return render_template('books_edit.html', book=book)

@app.route('/books/<int:book_id>/update', methods=['post'])
def update_book(book_id):
    if(Book.validate(request.form)):
        data = {
            **request.form,
            'id':book_id
        }
        Book.update(data)
        return redirect('/books')
    return redirect('/books/<int:book_id>/edit')

@app.route('/books/<int:book_id>/destroy', methods=["post"])
def destroy(book_id):
    Book.destroy_book(book_id)
    return redirect('/books')

@app.route('/books/<int:book_id>/del_confirm')
def confirm(book_id):
    if not 'user_id' in session:
        return redirect('/')
    book = Book.get_by_id(book_id)
    return render_template('books_delete.html', book=book)