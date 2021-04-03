class Book:
    def __init__(self, name):
        self.name = name
        self._author = None

    # Right usage of private variable
    @property
    def author(self):
        return self._author


book_object = Book("secret key")


# for making a variable private we can use `_` but still we can access to it. it's a convention

# Don't do this
print(book_object._author)
