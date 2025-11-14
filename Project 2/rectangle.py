from shape import shape
class rectangle(shape):
  def __init__(self,width,height):
    self.__width=width
    self.__height=height
  
  def get_height(self):
    return self.__height

  def get_width(self):
    return self.__width
  
  def set_height(self,new_height):
    self.__height=new_height
  
  def set_width(self,new_width):
    self.__width=new_width
  
  def area(self):
    area=self.__height*self.__width
    return area