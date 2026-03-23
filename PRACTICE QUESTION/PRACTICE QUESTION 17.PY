class Book:
    def __init__(self, name):
        self.name = name
        print("Book added:", self.name)

    def __del__(self):
        print("Book removed:", self.name)

b1 = Book("Python")
del b1