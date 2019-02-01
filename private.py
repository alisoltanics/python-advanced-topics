class Book:
    def __init__(self, name):
        self.name = name
        self._author = None

book_object = Book("secret key")
# for making a variable private we can use `_` but still we can access to it. it's a convention
print(book_object._author)
