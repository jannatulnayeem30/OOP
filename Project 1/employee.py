class Employee:
  def __init__(self,fname,lname,email,sal):
    self.__first_name=fname
    self.__last_name=lname
    self.__email=email
    self.__salary=sal

  def get_first_name(self):
    return self.__first_name

  def set_first_name(self,name):
    self.__first_name=name

  def get_last_name(self):
    return self.__last_name

  def set_last_name(self,last_name):
    self.__last_name=last_name

  def get_email(self):
    return self.__email

  def set_email(self,em):
    self.__email=em

  def get_salary(self):
    return self.__salary

  def set_salary(self,sal):
    self.__salary=sal


  def __str__(self): #method overloading
    print("----------------------")
    print("| First Name:",self.__first_name,"|")
    print("| Last Name:",self.__last_name,"  |")
    print("| Email Address:",self.__email,"  |")
    print("| Salary:",self.__salary,"        |")
    return "---------------------"
