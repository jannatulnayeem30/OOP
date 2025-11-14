from expense import Expense

class Savings(Expense):

    def __init__(self, amount, category, description,bank_name):
        super().__init__(amount, category, description)
        self.__bank_name=bank_name
    
    def get_bank_name(self):
        return self.__bank_name
    def set_bank_name(self,new_bank):
        self.__bank_name=new_bank 
    
    def calculate_expense(self):
        return Expense.get_amount(self)
    

