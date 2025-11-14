from manager import Manager

class employeerunner:
  list_of_managers=list()
  def create_manager(self,fname,lname,email,sal,dept,bonus):
    manager=Manager(fname,lname,email,sal,dept,bonus)
    employeerunner.list_of_managers.append(manager)
  def see_all_managers(self):
    for i in employeerunner.list_of_managers:
      print(i)


run=employeerunner()
run.create_manager("nayeem","nayeb","nayebnayeem@gmail",1000,"CSE",500)
run.create_manager("shah","nawaj","shahnawaj@gmail",1000,"CSE",500)
run.see_all_managers()
