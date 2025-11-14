from expense import Expense

class DailyExpense(Expense):

    def __init__(self,amount,category,description,days_tracked):
        super().__init__(amount,category,description)
        self.__days_tracked=days_tracked
    
    def get_days_tracked(self):
        return self.__days_tracked
    def set_days_tracked(self,new):
        self.__days_tracked=new
    
    def calculate_expense(self):
        return Expense.get_amount(self)
    
