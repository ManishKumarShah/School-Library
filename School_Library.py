class Library:
    def __init__(self,listofBooks):
        self.books = listofBooks

    def displayAvilablebooks(self):
        print("Books avilable in this library are : ")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} book .Please keep it safe and return within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry ,this book is already issued to someone else .")   
            print("Please wait until book avilable or try another books.")
            return False
            
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book on time .Hope you enjoyed reading.")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow :")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
        
if __name__ == "__main__":
    studentLibrary = Library(["Algorithms", "Discerte Structure ","DBMS", "M-1" ,"M-2","BCE","BEE","BME" ,"Atomic Habbit","Jungle Book","Current Affair"])
    student = Student() 
    menu ='''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
    while True:
        print(menu)
        a= int(input("Enter a Choice :"))
        if a == 1:
            studentLibrary.displayAvilablebooks()
        elif a==2:
            studentLibrary.borrowBook(student.requestBook())
        elif a==3:
            studentLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing a Student Library . Have a great day ahead!!")
            exit()             
        else:
            print("Invalid Chooice!")
