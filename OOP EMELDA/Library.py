class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"{book} has been added to the library.")
    
    def list_books(self):
        if self.books:
            print(f"Books in {self.name} Library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")

# Example of creating an object
library1 = Library("City Library", "Downtown")
library1.add_book("To Kill a Mockingbird")
library1.add_book("Pride and Prejudice")
library1.list_books()
