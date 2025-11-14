from patient import Patient
from doctor import Doctor
from appointment import Appointment

d1=Doctor("Nayeem",35,"Medicine",1500)
print(d1)
d1.add_schedule("Sun","9:00AM -11:00AM")
d1.see_schedule()
print("----------------------")
p1=Patient("Nahid",25)
print(p1)

new_ap=Appointment(d1,p1)
print(new_ap.show_visit_fee())
d1.get_appointment(new_ap.a_id)
print(d1.see_total_appointment())
new_ap.cancel_appointment()
print(d1.see_total_appointment())

"""d1.write_prescription(p1,["A","B","C"],"visit after one week")
p1.get_medical_history()"""