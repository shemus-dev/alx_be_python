class Book:
    """
    A class to represent a Book with title, author, and publication year.
    Implements magic methods for initialization, destruction, and representation.
    """
    
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        Returns an informal, user-friendly string representation.
        
        Returns:
            str: String in format "Title by Author, published in Year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Returns an official, unambiguous string representation that could recreate the object.
        
        Returns:
            str: String that looks like a Book constructor call
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"