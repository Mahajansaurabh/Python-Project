class Library:

    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def display(self):
        print('Books present in the library are: ')
        for book in self.books:
            print(' *'+ book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f'You havae been issued {bookName}.Please keep it safe and return it within 30 days')
            self.books.remove(bookName)
        else:
            print('Sorry,This book is either not available or has already been issued to someone else.Please wait until the book is available')

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!')

class Student:
    def requestBook(self):
        self.book = input('Enter the name of the book you want to borrow: ')
        return self.book

    def returnBook(self):
        self.book = input('Enter the name of the book you want to return')
        return self.book


class Student:
    pass

if __name__ == 'main':
   centraLibrary = Library(['Algorithms','Django','Clrs','Python'])
   student = Student()
   centraLibrary.displayAvailableBooks()
   while (True):
       welcomeMsg = '''
       ===== Welcome to Central Library =====
       Please choose an option:
       1. Listing all the books
       2. Request a book
       3. Add/Return a book
       4. Exit the library'''

       print(welcomeMsg)
       a = int(input('Enter a choice: '))
       if a == 1:
           centraLibrary.displayAvailableBooks()
       elif a==2:
           centraLibrary.borrowBook(student.requestBook())
       elif a==3:
           centraLibrary.returnBook(student.returnBook())
       elif a==4:
           print('Thanks for chooing Central Library! Have a great day ahead.')
           exit()
       else:
           print('Invalid Choice!')



