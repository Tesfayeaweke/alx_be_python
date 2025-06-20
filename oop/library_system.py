class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
    def list_books(self):
        for item in self.books:
            if hasattr(item,'file_size'):
                print(f"{item.__class__.__name__}: {item.title} by {item.author}, File Size: {item.file_size}")
            elif hasattr(item,'page_count'):
                print(f"{item.__class__.__name__}: {item.title} by {item.author}, Page Count: {item.page_count}")
            else:
                print(f"{item.__class__.__name__}: {item.title} by {item.author}")


