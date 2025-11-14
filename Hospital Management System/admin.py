from appointment import Appointment
from patient import Patient
from doctor import Doctor

class Admin:

    def entry_patient(self,name,age):
        self.pt=Patient(name,age)
        return self.pt
    
    def entry_doctor(self,name,age,specialty,visit):
        self.doc=Doctor(name,age,specialty,visit)
        return self.doc
    
    def create_appointment(self,d,p):
        self.appnt=Appointment(d,p)
        d.get_appointment(self.appnt.a_id)
        print("Appointment Placed Under Doctor",d.get_name())
        return self.appnt
    
    
     
         

           
             
        
    

