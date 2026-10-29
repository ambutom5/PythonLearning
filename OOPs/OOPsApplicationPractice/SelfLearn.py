class LibraryManagement:
    def __init__(self):
        self.books = []
        self.books_issued = {}

    def add_book(self):
        book = input("Enter the book to be added: ")
        self.books.append(book)
        print("Book added to the library!")

    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available!")
        else:
            i = 1
            for book in self.books:
                print(f"{i}. {book}")
                i += 1

    def borrow_book(self):
        book = input("Enter the book to borrow: ")
        if book in self.books:
            borrower = input("Enter Borrower Name: ")
            self.books.remove(book)
            self.books_issued[book] = borrower
            print(f"{book} issued to {borrower}")
        elif book in self.books_issued:
            print(f"{book} was issued to {self.books_issued[book]}")
        else:
            print("Book Not Found In The Library!")

    def return_book(self):
        book = input("Enter the book to return: ")
        if book in self.books_issued:
            borrower = self.books_issued.pop(book)
            print(f"{book} returned by {borrower}")
            self.books.append(book)
        else:
            print("This book was not issued here!")

    def search_book(self):
        book = input("Enter the book to search: ")
        if book in self.books:
            print("Book Available!")
        elif book in self.books_issued:
            print(f"{book} was issued to {self.books_issued[book]}")
        else:
            print("Book Not Available!")

obj = LibraryManagement()

while True:
    print("------------Library Management----------")
    print("1. Add Book")
    print("2. Display Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.add_book()
    elif choice == 2:
        obj.display_books()
    elif choice == 3:
        obj.borrow_book()
    elif choice == 4:
        obj.return_book()
    elif choice == 5:
        obj.search_book()
    elif choice == 6:
        break
    else:
        print("Invalid Choice!")