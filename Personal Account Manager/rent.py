from expense import Expense

class RentPayment(Expense):

    def __init__(self,amount,category,description,rent_type):
        super().__init__(amount,category,description)
        self.__rent_type=rent_type
    
    def get_rent_type(self):
        return self.__rent_type
    def set_rent_type(self,new):
        self.__rent_type=new
    
    def calculate_expense(self):
        return Expense.get_amount(self)
    