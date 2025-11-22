import json

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "available"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "status": self.status}


class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    def save_data(self):
        data = [b.to_dict() for b in self.books]
        json.dump(data, open("books.json", "w"), indent=4)

    def load_data(self):
        try:
            data = json.load(open("books.json", "r"))
            for d in data:
                b = Book(d["title"], d["author"], d["isbn"])
                b.status = d["status"]
                self.books.append(b)
        except:
            self.books = []

    def add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        self.books.append(Book(title, author, isbn))
        self.save_data()
        print("Book added")

    def issue_book(self):
        isbn = input("ISBN: ")
        for b in self.books:
            if b.isbn == isbn and b.status == "available":
                b.status = "issued"
                self.save_data()
                print("Issued")
                return
        print("Not available")

    def return_book(self):
        isbn = input("ISBN: ")
        for b in self.books:
            if b.isbn == isbn:
                b.status = "available"
                self.save_data()
                print("Returned")
                return
        print("Not found")

    def view_all(self):
        for b in self.books:
            print(b.title, "-", b.status)


lib = Library()

while True:
    print("\n1 Add  2 Issue  3 Return  4 View  5 Exit")
    ch = input(">> ")
    if ch == "1": lib.add_book()
    elif ch == "2": lib.issue_book()
    elif ch == "3": lib.return_book()
    elif ch == "4": lib.view_all()
    elif ch == "5":
        print("Exited")
        break
    else:
        print("Invalid option")
