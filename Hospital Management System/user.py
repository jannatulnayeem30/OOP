
class User():
    ID=0
    def __init__(self,name,age):
        User.ID+=1
        self.__name=name 
        self.__age= age
        self.__id=User.ID
        self.__role=None 
    
    def set_name(self,new_name):
        self.__name=new_name
    
    def set_age(self,new_age):
        self.__age=new_age
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
   
    
