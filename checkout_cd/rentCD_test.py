import unittest
import datetime
from datetime import timedelta
from rentCD import RentCD

class rentCDTest(unittest.TestCase):

    def setUp(self):
        self.rent_cd = RentCD()

    def test_customer_list_is_not_initially_empty(self):
        self.assertGreater(len(self.rent_cd.customer_list),0)

    def test_cd_list_is_not_initially_empty(self):
        self.assertGreater(len(self.rent_cd.cd_list), 0)

    def test_get_customer_name(self):
        self.assertEqual(self.rent_cd.get_customer_name('001'), 'Air')
        self.assertEqual(self.rent_cd.get_customer_name('002'), 'Net')

    def test_customer_does_exist(self):        
        self.assertIn('002' ,self.rent_cd.customer_list)

    def test_customer_does_not_exist(self):
        self.assertEqual('Customer not found',\
        self.rent_cd.get_customer_name('003'))

    def test_cd_does_exist(self):
        self.assertIn('1',self.rent_cd.cd_list)

    def test_checkout(self):        
        d1 = datetime.datetime.now() + timedelta(days=2)
        self.assertEqual("Net (002) rented Pride and Prejudice (3)" \
        " Rental Due: " + d1.strftime("%m/%d/%Y"), \
        self.rent_cd.checkout('002', '3'))
        self.assertGreater(len(self.rent_cd.cd_rented), 0)

    def test_checkout_if_cd_already_rented(self):
        
        self.assertEqual("Air (001) rented Fantasia 1999 (2) Rental Due:" \
        " 11/26/2014",\
        self.rent_cd.checkout('001', '2'))
        self.assertEqual('CD already rented',\
        self.rent_cd.checkout('001', '2'))

    def test_checkout_if_customer_id_is_invalid(self):

        self.assertEqual("Customer id is invalid",\
        self.rent_cd.checkout('01', '3'))

    def test_checkout_if_cd_id_is_invalid(self):
        self.assertEqual('CD id is invalid/CD not found',\
        self.rent_cd.checkout('002', '40'))

    
