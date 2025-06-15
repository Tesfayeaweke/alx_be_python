class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        if book not in self._books:
            return self._books.append(book)
        else:
            print("book already exists.")

    def check_out_book(self,title):
        

        
        
        
    



if __name__ == "__main__":
    # lib = Library()
    # lib.add_book(Book("Brave new world", "Aldus"))
    b = Book("Brave new world", "Aldus")
    print (b)