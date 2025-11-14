from abc import ABC, abstractmethod
class Expense(ABC):

    def __init__(self,amount,category,description):
        self.__amount=amount 
        self.__category=category 
        self.__description=description
    
    def get_amount(self):
        return self.__amount 
    def set_amount(self,new_amount):
        self.__amount=new_amount
    def get_category(self):
        return self.__category
    def set_category(self,new_category):
        self.__category=new_category
    def get_description(self):
        return self.__description
    def set_description(self,new_desc):
        self.__description=new_desc 
    
    @abstractmethod
    def calculate_expense(self):
        pass 