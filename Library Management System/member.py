from book import Book

class Members:
  ID=0
  def __init__(self,name,address,contact_no):
    Members.ID+=1
    self.__name=name
    self.__address=address
    self.__phone=contact_no
    self.id=Members.ID
    self.borrowed_books=list()
  
  def return_book(self,book):
    book.return_book()

  def borrow_request(self,book):
    if book.borrow_book() == True:
       self.borrowed_books.append(book)
       print("Dear "+self.__name+", You have successfully borrowed the book "+book.get_name()+" written by "+book.get_author()+" from our Library.")
       print ("PLEASE RETURN the book within 7 days to avoid any fine.") 
    else:
       print ("Request Failed. Book is loaned to other members")

  def display_info(self):
    print("Name: "+self.__name)
    print("Membership ID: " +str(self.id))
    print("Phone No:"+str(self.__phone))