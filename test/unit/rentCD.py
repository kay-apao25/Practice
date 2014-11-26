import datetime
from datetime import timedelta 

class RentCD(object):

    def __init__ (self):
        self.customer_list = {'001' : 'Air', '002' : 'Net', '003' : 'Gold', \
        '004' : 'Rain'}
        self.cd_list = {'1' : 'Twila Paris Hits', '2' : 'Fantasia 1999', \
        '3' : 'Pride and Prejudice', '4' : 'Timeless Songs'}
        self.cd_rented = {}
        self.num_cust_rented = {'001' : 0, '002' : 0}
        self.cust_rental_due = {}
        self.cd_rental_due = {'1': 2, '2': 3, '3': 3, '4': 2}

    def get_customer_id(self, customer_id):
        if self.customer_list.has_key(customer_id):
            return "1.1"
        else:
            return '1'
             
    def get_cd_id(self, cd_id):
        if self.cd_list.has_key(cd_id):
            return "2.1"
        else:
            return '2'

    def check_if_rented(self, cd_id):
        if self.cd_rented.has_key(cd_id):
            return '3'
        else:
            return self.cd_rented


    def cd_rental_limit(self, customer_id):
        if self.num_cust_rented[customer_id] == 3:
            return '4'
        else:
            return '4.1'

    def late_rental(self, customer_id):
        d1 = datetime.datetime.now() + timedelta(days=3)
        
        if self.cust_rental_due.has_key(customer_id):
           if self.cust_rental_due[customer_id] <  d1.strftime("%m/%d/%Y"):
               return '5' 
        else:
           return '5.1'

    def checkout(self, customer_id, cd_id):
        if self.get_customer_id(customer_id) == '1':
            return 'Customer id is invalid'
        elif self.get_cd_id(cd_id) == '2':
            return 'CD id is invalid/CD not found'
        elif self.check_if_rented(cd_id) == '3':
            return 'CD already rented'
        elif self.cd_rental_limit(customer_id) == '4':
            return 'CD rental limit reached'
        elif self.late_rental(customer_id) == '5':
            return 'Customer has late rental'
        else:
            self.cd_rented[cd_id] = customer_id
            self.num_cust_rented[customer_id] = self.num_cust_rented[customer_id] + 1
            d1 = datetime.datetime.now() + timedelta(days=self.cd_rental_due[cd_id])
            self.cust_rental_due[customer_id] = d1.strftime("%m/%d/%Y")

            return self.customer_list[customer_id] + \
            " (" + customer_id  + ") rented " + \
            self.cd_list[cd_id]  + " (" + cd_id + ") " \
            "Rental Due: " + d1.strftime("%m/%d/%Y")
