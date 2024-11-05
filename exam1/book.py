class Book:
    '''
    The assignment said two constructors, but I don't think python really does that, 
    so we'll simulate it with default values. This way we can call it with either
    Book(isbn="123456") or Book(title="How To Succeed In Python Without Really Trying", author="Bryan Choate").

    If I were doing this for any sort of production application, "author" would be a 
    separate class, and we'd use an enum or dict for category. We'd also create a shopping 
    cart of some sort so you can checkout with multiple books at once. But we're on the clock
    for this exam, so we'll keep it pretty simple.
    '''
    def __init__(self, isbn=None, title=None, author=None):
        # We need to set default values since it's a single constructor
        self.__isbn = isbn if isbn else ''
        self.__title = title if title else ''
        self.__author = author if author else ''
        self.__category = ''
        self.__price = 0.0
        self.__page_count = 0

    # Getters
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_page_count(self):
        return self.__page_count

    # Setters
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_category(self, category):
        self.__category = category

    def set_price(self, price):
        self.__price = price

    def set_page_count(self, page_count):
        self.__page_count = page_count

    # Get some book details from the user
    def input_book_details(self):
        self.__isbn = input("Enter ISBN: ")
        self.__title = input("Enter Title: ")
        self.__author = input("Enter Author: ")
        self.__category = input("Enter Category: ")
        self.__price = float(input("Enter Price: "))
        self.__page_count = int(input("Enter Page Count: "))

    # 7% is pretty low for sales tax, but we'll go with it
    def purchase(self, quantity):
        total_price = self.__price * quantity
        tax = total_price * 0.07
        return total_price + tax

    # SHow the book info, etc
    def display(self):
        print(f"ISBN: {self.__isbn}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Category: {self.__category}")
        print(f"Price: {self.__price}")
        print(f"Page Count: {self.__page_count}")

    # Compare by either ISBN or title & author combo; no need for variables
    def is_same_book(self, other_book):
        return self.__isbn == other_book.get_isbn() or \
               (self.__title == other_book.get_title() and self.__author == other_book.get_author())
