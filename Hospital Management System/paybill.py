from abc import ABC,abstractmethod
class Paybill(ABC):

    @abstractmethod
    def pay_method(self,invoice):
        pass 

class Credit_Card(Paybill):

    def pay_method(self,invoice,card_no):
        print ("Total Fee: "+str(invoice)+ "debited from your account")
        return "Payment Successfull"

class Hand_cash(Paybill):

    def pay_method(self, invoice, amount):
        if invoice<amount:

            print("Payment Successful")
            print ("Remaining amount to be collected "+str (amount-invoice))
        elif invoice>amount:
            print ("Insufficient Amount")
        
        else:
            print ("Payment Successful")
