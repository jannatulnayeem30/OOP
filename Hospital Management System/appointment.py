from doctor import Doctor
from patient import Patient 
class Appointment:
    apt_id=0
    def __init__(self,doc,pat):
        Appointment.apt_id+=1
        self.d=doc 
        self.p=pat 
        self.d_id=self.d.get_id()
        self.p_id=self.p.get_id()
        self.a_id=Appointment.apt_id

    def show_visit_fee(self):
        return self.d.get_visit_fee() 
    
    def cancel_appointment(self):
        for i in range(len(self.d.app)):
            appointment_to_remove=self.a_id
            if self.d.app[i]==self.a_id:
                self.d.app.remove(appointment_to_remove)
                print("Appointment Cancelled")
                

