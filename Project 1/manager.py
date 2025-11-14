from employee import Employee
class Manager(Employee):

  def __init__(self,fname,lname,email,sal,dept,bonus):
    super().__init__(fname,lname,email,sal) #ParentClass_constructor inherited and extended
    self.__dept=dept
    self.__bonus=bonus

  def get_dept(self):
    return self.__dept
  def set_dept(self,dep):
    self.__dept=dep

  def get_bonus(self):
    return self.__bonus
  def set_bonus(self,b):
    self.__bonus=b

  def __str__(self):
    super().__str__()   #ParentClass method overriding
    print("----------------------")
    print("|","Department",self.__dept,"|")
    print("|","Employee Bonus",self.__bonus,"|")
    return "----------------------"