# As a home exercise, try creating a class from a book you would read. Think about how you would write its class and what properties it should have.


class Book:
    def __init__(self, title, author, isbn="unknown"):
        self.title = title
        self.author = author
        self.isbn = isbn


book1 = Book("Advanced Engineering Mathematics", "Erwin Kreyszig", 9780470458365)
book2 = Book("Machine Design", "R.S. Khurmi")
print(
    f"A book you would read is {book1.title} written by {book1.author}. Its ISBN number is {book1.isbn}."
)
print(
    f"Another book you would read is {book2.title} written by {book2.author}. Its ISBN number is {book2.isbn}."
)
