from book import Book

# Let's build a library of books
book1 = Book(isbn="123456")
book2 = Book(title="How To Succeed In Python Without Really Trying", author="Bryan Choate")
book3 = Book() # We'll add this later

# Input details for the third book
book3.input_book_details()

# Test the purchase method with a quantity of 2 for the first book
book1.set_price(49.99) # Full price, but it's worth it
total_cost = book1.purchase(2)
print(f"Total cost for 2 copies of ${book1.get_title} (with tax): ${total_cost:.2f}")

# Test the display method
print("\nBook 1 Details:")
book1.display()

print("\nBook 2 Details:")
book2.set_isbn("123456") # Set the ISBN to match book 1, the greatest book of all time
book2.set_price(44.99) # I don't write for free, and this is with 10% off, so act now!
book2.set_category("Programming") # It's the only programming book you'll ever need
book2.set_page_count(3000) # Most of this is stories about my dogs, who prefer javascript
book2.display()

print("\nBook 3 Details:")
book3.display()

# Test the is_same_book method
print("\nChecking if Book 1 and Book 2 are the same:")
if book1.is_same_book(book2):
    print("Book 1 and Book 2 are the same.")
else:
    print("Book 1 and Book 2 are different.")

print("\nChecking if Book 1 and Book 3 are the same:")
if book1.is_same_book(book3):
    print("Book 1 and Book 3 are the same.")
else:
    print("Book 1 and Book 3 are different.")
