from user import User

class Patient(User):
    def __init__(self,name,age):
       super().__init__(name,age)
       self.__medical_history=[]
       self.__role="Patient"
       
    def __str__(self):

       return "Patient"+" Name: "+Patient.get_name(self)+" Age: "+str(Patient.get_age(self))+" "+"Patient"+" ID: "+str(Patient.get_id(self))


    def get_roles(self):
        return self.__role
    
    def add_medical_history(self,medicine,comment):
        hist={"med":medicine,"cmnt":comment}
        self.__medical_history.append(hist)
    
    def get_medical_history(self):
        for i in self.__medical_history:
            print(i)    

    def see_doctorX_schedule(self,doc):
        doc.see_schedule()

    
 

        
         


