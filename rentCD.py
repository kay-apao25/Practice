from customer import Customer

class RentCD(object):

    def __init__ (self):
        self.customer_list = {}
        self.cd_list = {"1", "2", "3", "4", "5"}

    def add_customer(self, customer):
        self.customer_list[customer.id] = customer.id 
