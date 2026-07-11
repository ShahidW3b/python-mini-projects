print("==================================")
print(" Personal Book Collection Manager ")
print("==================================")

books = {}

while True: 
    print("\n1. Add a new book")
    print("2. Show all books")
    print("3. Search for a book by title")
    print("4. Update the reading status")
    print("5. Remove a book")
    print("6. Count total books")
    print("7. Show finished books")
    print("8. Exit")
    print("-----------------------------------")


    Chose = input("Chose an option (1 - 8): ")

    if Chose == "1": 

        print("\n---------- ADD A BOOK  ----------")

        title = input("Enter the book title: ").title()
        
        if title in books: 
            print("This book already exists.")

        else: 
            
            author = input("Enter the book author: ").title()
            genere = input("Enter the genere: ").title()
            year = int(input("Enter the publication year: "))
            status = input("Enter reading status" 
            "(Read / Currently Reading / Not Read): "
            ).title()

            books[title] = {
                "author" : author,
                "genre" : genere,
                "year" : year,
                "status" : status
            }


        print(f"{title} was added successfully.")
        print("------------------------------------")


    elif Chose == "2": 

        print("\n---------- ALL BOOKS ----------")

        if len(books) == 0: 
            print("No book available.")


        else: 
            book_number = 1

            for title, information in books.items():
                print(f"\n Book {book_number}")
                print(f"Title : {title}")
                print(f"Author : {information['author']}")
                print(f"Genre : {information['genre']}")
                print(f"Year: {information['year']}")
                print(f"Reading Status : {information['status']}")
                print("-----------------------------------------")

                book_number += 1


    elif Chose == "3": 

        print("\n---------- SEARCH FOR A BOOK  ----------")

        search = input("Enter book tilte to search: ").title()

        if search in books: 
            information = books[search]

            print(f"\n Book Found.")
            print(f"Title : {search}")
            print(f"Author : {information['author']}")
            print(f"Genre : {information['genre']}")
            print(f"Year : {information['year']}")
            print(f"Reading Status : {information['status']}")

        
        else: 
            print("Book not found.")
            print("---------------------------------------")



    elif Chose == "4": 

            print("\n---------- UPDATE READING STATUS ----------")

            title = input("Enter the book tilte: ").title()

            if title in books: 
                print(f"Current status: {books[title]['status']}")

                new_status = input("Enter new status "
                "(Read / Currently Reading / Not Read): "
                ).title()
                
                books[title]["status"] = new_status

                print(" Reading status updated successfully.")

            else: 
                print("Book not found.")
                print("-------------------------------------")



    elif Chose == "5": 

        print("\n---------- REMOVE A BOOK  ----------")
        
        title = input("Enter a book to remove: ").title()

        if title in books: 
            del books[title]
            print(f"{title} was removed successfully.")
        
        else: 
            print("Book not found.")
            print("---------------------------------------------")


    
    elif Chose == "6": 
        
        print("\n---------- TOTAL BOOKS  ----------")

        print(f"Total number of books:  {len(books)}")
        print("-----------------------------------------")

    

    elif Chose == "7": 

        print("\n---------- FINISHED BOOKS  ----------")

        finished_books = 0
        
        for title, information in books.items():
            if information["status"] == "Read": 
                print(f"Title : {title} ")
                print(f"Author : {information['author']}")

                finished_books += 1

        if finished_books == 0: 
            print("No finished books available.")

        else:
            print(f"Totla finished books: {finished_books}")



    elif Chose == "8": 
        
        print("\n---------- EIXT  ----------")

        print("========================================")
        print("Thank you for using the Book COllection  System.")
        print("Goodbye!")
        print("========================================")
        break
        


    else: 
        print("Invalind input. Please chose from 1 to 8")
    

        

        
       





