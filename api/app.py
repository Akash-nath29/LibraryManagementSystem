from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100))
    is_available = db.Column(db.Boolean, default=True)
    
    def addBook(self, name, author, is_available):
        self.name = name
        self.author = author
        self.is_available = is_available
        db.session.add(self)
        db.session.commit()
        return self
    
    def deleteBook(self, id):
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return book
    
    def lendBook(self, book):
        book.is_available = False
        db.session.commit()
        return book
    
    def returnBook(self, id):
        book = Book.query.get(id)
        book.is_available = True
        db.session.commit()
        return book
    
    def __repr__(self):
        return '<Book %r>' % self.name
    
@app.route('/')
def getBooks():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {}
        book_data['id'] = book.id
        book_data['name'] = book.name
        book_data['author'] = book.author
        book_data['is_available'] = book.is_available
        output.append(book_data)
    return jsonify(output)

@app.route('/getBook/<int:id>', methods=['GET', 'POST'])
def getBook(id):
    book = Book.query.get(id)
    book_data = {}
    book_data['id'] = book.id
    book_data['name'] = book.name
    book_data['author'] = book.author
    book_data['is_available'] = book.is_available
    return jsonify(book_data)

@app.route('/lend-book/<int:id>', methods=['GET'])
def lend_book(id):
    book = Book.query.get(id)
    book.lendBook(book)
    return jsonify({
        'name': book.name,
        'author': book.author,
        'is_available': book.is_available
    })

@app.route('/return-book', methods=['POST'])
def returnBook():
    id = request.json['id']
    book = Book()
    return jsonify(book.returnBook(id))

@app.route('/addBook')
def addBook():
    book_one = Book(name="Rich Dad Poor Dad", author="Robert T Kiyosaki")
    book_two = Book(name="Think and Grow Rich", author="Napolion Hill")
    book_three = Book(name="Physics", author="RD verma")
    book_four = Book(name="Mathematics", author="Akash Nath")
    # book_one = Book(name="Rich Dad Poor Dad", author="Robert T Kiyosaki")
    # book_one = Book(name="Rich Dad Poor Dad", author="Robert T Kiyosaki")

    db.session.add(book_one)
    db.session.commit()
    db.session.add(book_two)
    db.session.commit()
    db.session.add(book_three)
    db.session.commit()
    db.session.add(book_four)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)