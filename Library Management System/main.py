from book import Book
from member import Members
from library import Library

def main():
    member1=Members("Nayeem","Uttara","01792065803")
    member2=Members("Fahim","Khilkhet","01792065804")

    book1=Book("Capital","Karl Marx","isbxxx45")
    book2=Book("Social","Mamdani","isbxxx46")

    Lib=Library([book1,book2],[member1,member2])

    member1.borrow_request(book1)
    print("-----------------------")
    print("Another member will try to borrow the same book lend by other")
    print("------------------------")
    member2.borrow_request(book1)
    print("------------------------")
    member2.borrow_request(book2)
    print("------------------------")
    book3=Book("Book3","Author 3","isbxxxx47")
    Lib.add_book(book3)
    print("------------------------")
    member3=Members("Fahad","Denmark","65498324")
    Lib.add_member(member3)
    print("------------------------")
    member3.borrow_request(book3)
    Lib.display_library_info()
    print("-------------------------")
    member2.display_info()
    print("------------------------")
if __name__ == "__main__":
    main()