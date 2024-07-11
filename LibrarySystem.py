class library:
    def __init__(self,listofBooks):
        self.booklist=listofBooks
    def displayAvialableBook(self):
        print("\nAvialable Books are:\n")
        i=0
        for book in self.booklist:
            print(str(i)+"-> "+ book)
            i=i+1
            print("\n")
    def borrowBOOK(self,book):
        if book in self.booklist:
            print(f"\nYou have been issued {book} book.\n"
                  "Please keep it safe and return it within 30 days\n")
            self.booklist.remove(book)
        else:
            print(f"Sorry, {book} book is not available right now\n")

    def returnBOOK(self,book):
        self.booklist.append(book)
        print(f"Thanks for returning {book}\n")

        
    

if __name__=='__main__':
    Centreal_library=library(["Python","Java","C++","C","Data Structure","Operating System"])
    print("WELCOME TO CENTRAL LIBRARY\n")
    while(True):
                 print("Enter your choice:\n1. List of books in library\n2. Request for Book \n3. Return a Book\n4. Exit Library")
        
                 user_choice=int(input("Enter your choice:"))
                 if user_choice==1:
                             Centreal_library.displayAvialableBook()
                 elif user_choice==2:
                             book=input("Enter the name of the book you want to borrow: ")
                             Centreal_library.borrowBOOK(book)
                 elif user_choice==3:
                             book=input("Enter the book name Which you want to Return:")
                             Centreal_library.returnBOOK(book)
                 else:
                       print("\nThank you for using The library\n")
                       exit()
       

#Problem Statement- Implement a student library system [controlled by menu system],
#using OOPs where Students can Borrow from the list/ Add(return) Books in the list
#with separate library class


