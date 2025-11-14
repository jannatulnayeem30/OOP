from dailyexpense import DailyExpense
from loan import LoanPayment
from rent import RentPayment
from savings import Savings
from income import Income
from income import Income
from account_manager import AccountManager
class User:

    def __init__(self,name,age):
        self.__name=name 
        self.__age=age 
        self.__acm=AccountManager() #object of AccountManager class 

    def add_income(self,income_amount,source):
        self.income=Income(income_amount,source)
        self.__acm.add_income(self.income)  


    def add_expense(self):
        description=input("Enter Expense Description: ")
        amount=int(input("Enter Amount: "))
        print("A) Enter 1 for Daily Expense")
        print("B) Enter 2 for Bank Savings")
        print("C) Enter 3 for Loan Payment")
        print("D) Enter 4 for Utility Bill")
        category=int (input("Enter Category: "))

        if category==1:
            days_tracked=int (input("Enter the expense of total days: "))
            self.dailyexpense=DailyExpense(amount,category,description,days_tracked)
            self.__acm.add_expense(self.dailyexpense)
        
        elif category==2:
            bank_name=str (input("Enter the Bank Name: "))
            self.Savings=Savings(amount,category,description,bank_name)
            self.__acm.add_expense(self.Savings) 
        
        elif category==3:
            loan_type=str (input("Enter the Loan type: "))
            self.loan_pay=LoanPayment(amount,category,description,loan_type)
            self.__acm.add_expense(self.loan_pay) 
        
        else:
            rent_type=str (input("Enter the name of bill: "))
            self.rent=RentPayment(amount,category,description,rent_type)
            self.__acm.add_expense(self.rent) 

     
    def view_summary(self):
       print("Summary")
       return self.__acm.generate_report()    

        
