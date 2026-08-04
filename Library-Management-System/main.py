class BOOK:
    def __init__(
        self, 
        title, 
        author,
        pages,
        year
        
    ):

        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        
        self.available = True
    
    def describe_book(self): 
        print("==== Book Detials ====")
        print(
            f"Title : {self.title.title()}\n"
            f"Author : {self.author.title()}\n"
            f"Number of pages : {self.pages}\n"
            f"Publication year : {self.year}\n"

            )

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Successfully borrowed.")

        else: 
            print("Book is already borrowed.")

    def return_book(self):
        if self.available:
            self.available = True

            print("Book returned successfully.")
        
        else: 
            print("Book is not returned.")

    
book = BOOK("Hundered years of solitute", "Gabriel Garcia Marquez", 540, 1980 )


while True:
    print("===== Library System =====")
    print("1. Show book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")


    chose = input("Chose an option (1-4): ")

    if chose == "1":
        book.describe_book()

    elif chose == "2": 
        book.borrow_book()


    elif chose == "3": 
        book.return_book()

    elif chose == "4": 
        print("Thanks for chosing our Library.")
        print("Exiting...")
        break

    else: 
        print("Invalid input. please chose from 1-4.")
    

