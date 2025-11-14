from shape import shape
import math
class circle (shape):

  def __init__(self,radius):
    self.__radius=radius

  def get_radius(self):
    return self.__radius
  def set_radius(self,new_radius):
    self.__radius=new_radius
  
  def area(self):
    radius=self.__radius
    area= math.pi*radius*radius
    return area
  
