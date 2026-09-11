class Library:
    def __init__(self):
        self.books = []
        self.issued_books = {}

    def add_book(self):
        book = input("Enter Book to Add: ")
        self.books.append(book)
        print("Book Added Successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available in the library!")
        else:
            i = 1
            for book in self.books:
                print(i,".",book)
                i += 1

    def issue_book(self):
        book = input("Enter Book to Borrow: ")
        if book in self.books:
            borrower = input("Enter Issuer Name: ")
            self.books.remove(book)
            self.issued_books[book] = borrower
            print(f"Book '{book}' Issued to {borrower}!")
        else:
            print("The book is not available in the library!")

    def return_book(self):
        book = input("Enter book to be returned: ")
        if book in self.issued_books:
            borrower = self.issued_books.pop(book)
            self.books.append(book)
            print(f"Book '{book}' returned by {borrower}!")
        else:
            print("This book was not issued!")

    def search(self):
        book = input("Enter book to be searched: ")
        if book in self.books:
            print("The book is available in the library!")
        elif book in self.issued_books:
            print(f"The book '{book}' is currently issued to {self.issued_books[book]}!")
        else:
            print("The book is not available in the library")


obj = Library()

while True:
    print("\n------ Library Management System ------")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.add_book()
    elif choice == 2:
        obj.display_books()
    elif choice == 3:
        obj.issue_book()
    elif choice == 4:
        obj.return_book()
    elif choice == 5:
        obj.search()
    elif choice == 6:
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid Choice! Please try again.")

