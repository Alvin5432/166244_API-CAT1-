class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}' by {book.author}.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books and book.mark_as_returned():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}' by {book.author}.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- '{book.title}' by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

def main_library():
    books = [
        Book("The Stranger", "Albert Camus"),
        Book("The Metamorphos", "Franz Kafka"),
        Book("Pride and Prejudice", "Jane Austen")
    ]

    member = LibraryMember("Alvin", "M001")

    while True:
        print("\nLibrary Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available books:")
            for i, book in enumerate(books):
                if not book.is_borrowed:
                    print(f"{i + 1}. {book.title} by {book.author}")
            book_choice = int(input("Enter the number of the book to borrow: ")) - 1
            if 0 <= book_choice < len(books):
                member.borrow_book(books[book_choice])
            else:
                print("Invalid choice.")
        elif choice == "2":
            print("Borrowed books:")
            for i, book in enumerate(member.borrowed_books):
                print(f"{i + 1}. {book.title} by {book.author}")
            book_choice = int(input("Enter the number of the book to return: ")) - 1
            if 0 <= book_choice < len(member.borrowed_books):
                member.return_book(member.borrowed_books[book_choice])
            else:
                print("Invalid choice.")
        elif choice == "3":
            member.list_borrowed_books()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_library()