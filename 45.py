
class publisher:
    def __init__(self, name):
        self.name = name
class book(publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author
class python(book):
    def __init__(self, name, title, author, price, page_no):
        super().__init__(name, title, author)
        self.price = price
        self.page_no = page_no
    def display(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Page Number:", self.page_no)
s1 = python("albin", "the book", "odin", 1500, 200)
s1.display()

