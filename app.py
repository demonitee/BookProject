from flask import Flask, render_template, request, url_for, redirect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from books import Books
from customers import Customers
from loans import Loans
import loader

app = Flask(__name__)

engine = create_engine("sqlite:///books.db", echo=True, future=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/book', methods=['GET', 'POST'])
def showbook():
    if request.method == 'GET': loader.removerow(Books, request.args.get('rowid'))
    return render_template('book.html', book=loader.getdata(Books))


@app.route('/customer', methods=['GET', 'POST'])
def showcustomer():
    return render_template('book.html', customer=loader.getdata(Customers))


@app.route('/addbook', methods=['POST', 'GET'])
def addAbook():
    if request.method == 'POST':
        newbook = Books(id=request.form.get('id'), name=request.form.get('name'), author=request.form.get('author'),
                        year_published=request.form.get('year_published'), type=request.form.get('type'))
        loader.addrow(newbook)
        return redirect('/')
    else:
        return render_template('addbook.html')


@app.route('/addcustomer', methods=['POST', 'GET'])
def addAcustomer():
    if request.method == 'POST':
        newcustomer = Customers(id=request.form.get('id'), name=request.form.get('name'), city=request.form.get('city'),
                                age=request.form.get('age'))
        loader.addrow(newcustomer)
        return redirect('/')
    else:
        return render_template('addcustomer.html')


if __name__ == "__main__":
    app.run(debug=True)
