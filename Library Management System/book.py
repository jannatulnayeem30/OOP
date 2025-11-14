class Book:
  def __init__(self,title,author,isbn):
    self.__title=title
    self.__author=author
    self.__isbn=isbn
    self.is_borrowed=False

  def get_name(self):
    return self.__title
  def get_author(self):
    return self.__author
    
  def borrow_book(self):
    if self.is_borrowed==False:
      self.is_borrowed=True
      print("Borrow request Accepted!")
      return True
    else:
      #print("The book is not available to borrow")
      return False
  def return_book(self):
    self.is_borrowed=False
    return "Thank you! The Book is returned successfully."    