class Book:
    """
    Base class representing a Book with title and author.
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def get_details(self):
        """
        Returns a string with book details.
        
        Returns:
            str: Formatted book details
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book, inherits from Book.
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size
    
    def get_details(self):
        """
        Returns a string with eBook details.
        
        Returns:
            str: Formatted eBook details
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book, inherits from Book.
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count
    
    def get_details(self):
        """
        Returns a string with print book details.
        
        Returns:
            str: Formatted print book details
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Class representing a library that manages a collection of books using composition.
    """
    
    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self.books = []  # Composition: Library contains books
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book: Instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
        print(f"Added: {book.title}")
    
    def list_books(self):
        """
        Print details of all books in the library.
        """
        print("\nLibrary Collection:")
        print("-" * 30)
        for book in self.books:
            print(book.get_details())