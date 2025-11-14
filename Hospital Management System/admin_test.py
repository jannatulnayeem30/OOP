from admin import Admin
from paybill import *
app=Admin()
doc1=app.entry_doctor("Munmun",32,"Medicine",1500)
print(doc1)
p1=app.entry_patient("Nayeem","27")
print(p1)
appoint=app.create_appointment(doc1,p1)
invoice=appoint.show_visit_fee()
#payment
payment=Hand_cash()
payment.pay_method(invoice,200)
print (doc1.see_total_appointment())
appoint.cancel_appointment()
print (doc1.see_total_appointment())