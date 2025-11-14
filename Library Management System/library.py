from book import Book
from member import Members
class Library:
   def __init__(self,book,member):
     self.__book=book
     self.__member=member

   def add_book(self,new_book):
     self.__book.append(new_book)
     print("Book Added to the Library!")
   def add_member(self,new_member):
     self.__member.append(new_member)
     print("New Member Added to the Library!")

   def display_library_info(self):
     print("Total No. of Books:",len(self.__book))
     print("Total Active Members:",len(self.__member))