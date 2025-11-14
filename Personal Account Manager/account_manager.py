from dailyexpense import DailyExpense
from income import Income
from loan import LoanPayment
from savings import Savings
from rent import RentPayment

class AccountManager:

    def __init__(self):
        self.__income=[] #income objects will be stored here
        self.__expense=[] #expense objects will be stored here

    def add_income(self,income):
        self.__income.append(income)

    def add_expense(self,expense):
        self.__expense.append(expense)    

    def get_total_income(self):
        total_income=0
        for i in self.__income:
            total_income=total_income+i.get_monthly_income()
        return total_income 
    def get_total_expense(self):
        total_expense=0
        for i in self.__expense:
            total_expense=total_expense+i.calculate_expense()
        return total_expense
    
    def get_balance(self):
        if len (self.__income) == 0:
            return "No Income"
        balance=self.get_total_income()-self.get_total_expense()
        return balance  
    
    def generate_report(self):
        total_income=self.get_total_income()
        total_expense=self.get_total_expense()
        balance=self.get_balance()
        print("Your Total Income:",total_income)
        print("Your Total Expense:",total_expense)
        print("Remaining Balance:",balance)
        if balance<0:
            return "Try to Save your money"
        else:
            return "Thank you"
        
