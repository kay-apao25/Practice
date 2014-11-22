import unittest
from cd import CD
from customer import Customer
from rentCD import RentCD

class rentCDTest(unittest.TestCase):

    def setUp(self):
        self.rent_cd = RentCD()

    def test_customer_list_is_initially_empty(self):
        self.assertEqual({}, self.rent_cd.customer_list)
        self.assertEqual(len(self.rent_cd.customer_list),0)

    def test_cd_list_is_not_initially_empty(self):
        self.assertEqual({"1", "2", "3", "4", "5"}, self.rent_cd.cd_list)
        self.assertGreater(len(self.rent_cd.cd_list), 0)

    def test_add_customer(self):

        customer_1 = Customer("1")
        customer_2 = Customer("2")
        
        self.rent_cd.add_customer(customer_1)
        self.rent_cd.add_customer(customer_2)
   
        self.assertEqual(len(self.rent_cd.customer_list),2)

    def test_customer_does_exist(self):
        
        customer_1 = Customer("1")
        customer_2 = Customer("2")
 
        self.rent_cd.add_customer(customer_1)
        self.rent_cd.add_customer(customer_2)

        self.assertIn("2",self.rent_cd.customer_list)

    def test_cd_does_exity(self):
        self.assertIn("5",self.rent_cd.cd_list)
