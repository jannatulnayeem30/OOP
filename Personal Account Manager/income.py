class Income:

    def __init__(self,monthly_income,income_source):
        self.__monthly_income=monthly_income
        self.__income_source=income_source
    
    def get_monthly_income(self):
        return self.__monthly_income 
    def set_monthly_income(self,new):
        self.__income_source=new

    def get_income_source(self):
        return self.__income_source
    def set_income_source(self,new):
        self.__income_source=new 

    