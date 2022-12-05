import random
from complex import Complex, minus_comlex, sum_comlex

class BookShelf():
    __shelf = []

    def __init__(self,books):
        self.books = books
        BookShelf.__add(self,self.books)

    def __add(self,books):
        for i in books:
            BookShelf.__shelf.append(i)

    def add_to_shelf(self,book):
        self.book=book
        BookShelf.__shelf.append(self.book)
        
    def del_from_shelf(self,book):
        self.book=book
        BookShelf.__shelf.remove(book)
        
    def shuffle_shelf(self):
        random.shuffle(BookShelf.__shelf)
        
    def pr(self):
        print(BookShelf.__shelf)


def main():

    print('\nTask 1')
    f = BookShelf(['hefuw','jefwuhf','fewhf','rgreg','regrgre','rgereg'])
    
    f.pr()
    f.add_to_shelf('book')
    f.pr()
    f.del_from_shelf('book')
    f.pr()
    f.shuffle_shelf()
    f.pr()

    print('\nTask 2')
    s1 = Complex(3,5)
    s2 = Complex(8,-9)
    s1.show()
    s2.show()
    print(sum_comlex(s1,s2))
    print(minus_comlex(s1,s2))

if __name__ == '__main__':
    main()
   