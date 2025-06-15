class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = not self._is_checked_out
        return self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        if book not in self._books:
            self._books.append(book)
        else:
            print("book already exists.")
        

    def check_out_book(self,title):
        for item in self._books:
            if item.title == title and item._is_checked_out == False:
                item._is_checked_out = item.check_out() 
                
                return True
        
            elif item.title == title and item._is_checked_out == True:
                
                print(f"{item.title}is checked out already can't checkout.")
                return False
            
    def return_book(self,title):
        for item in self._books:
           if item.title == title and item._is_checked_out == True:
               item._is_checked_out = item.check_out()
               return True
           elif item.title == title and item._is_checked_out == False:
               print("Item already available.")
               return False
           
    def list_available_books(self):
        for item in self._books:
            if not item._is_checked_out:
                print(f"{item.title} by {item.author}")

     
    
        
        
        

        
        
        
    



if __name__ == "__main__":
    ...
    