from expense import Expense

class LoanPayment(Expense):

    def __init__(self,amount,category,description,loan_type):
        super().__init__(amount,category,description)
        self.__loan_type=loan_type 
    
    def get_loan_type(self):
        return self.__loan_type
    def set_loan_type(self,new):
        self.__loan_type=new 
    
    def calculate_expense(self):
        return Expense.get_amount(self)
    
