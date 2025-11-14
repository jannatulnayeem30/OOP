from user import User
class Doctor(User):

    def __init__(self,name,age,specialty,visit):
        super().__init__(name,age)
        self.__specialty=specialty
        self.__schedule=[]
        self.__visit_fee=visit
        self.app=[]

    
    def get_visit_fee(self):
        print ("Doctor "+ Doctor.get_name(self) + " Visit fee: " + str (self.__visit_fee) + " Taka") 
        return self.__visit_fee
    def add_schedule(self,day,time):
        dic={day:time}
        self.__schedule.append(dic)     
    
    def see_schedule(self):
        for i in self.__schedule:
            print(i)

    def get_appointment(self,ap):
        self.app.append(ap)
    
    def see_total_appointment(self):
        return "Doctor " + Doctor.get_name(self)+ " Total Appointment: " + str (len(self.app))
    
    def write_prescription(self,patient,medicine,comment):
        patient.add_medical_history(medicine,comment)

    def __str__(self):

        return "Doctor "+" Name: "+Doctor.get_name(self)+" Age: "+str(Doctor.get_age(self))+" "+"Doctor "+" ID: "+str(Doctor.get_id(self))




    
    


