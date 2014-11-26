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

    def test_customer_does_exist(self):        
        self.assertIn('002' ,self.rent_cd.customer_list)

    def test_cd_does_exist(self):
        self.assertIn('1',self.rent_cd.cd_list)

    def test_checkout(self):        
        d1 = datetime.datetime.now() + timedelta(days=3)

        self.assertEqual("Net (002) rented Pride and Prejudice (3)" \
        " Rental Due: " + d1.strftime("%m/%d/%Y"), \
        self.rent_cd.checkout('002', '3'))
        self.assertGreater(len(self.rent_cd.cd_rented), 0)

    def test_checkout_if_cd_already_rented(self):
        d1 = datetime.datetime.now() + timedelta(days=3)
        self.assertEqual("Air (001) rented Fantasia 1999 (2) Rental Due: " \
        + d1.strftime("%m/%d/%Y"),\
        self.rent_cd.checkout('001', '2'))
        print self.rent_cd.check_if_rented('2')
        self.assertEqual('CD already rented',\
        self.rent_cd.checkout('002', '2'))

    def test_checkout_if_customer_id_is_invalid(self):

        self.assertEqual("Customer id is invalid",\
        self.rent_cd.checkout('01', '3'))

    def test_checkout_if_cd_id_is_invalid(self):
        self.assertEqual('CD id is invalid/CD not found',\
        self.rent_cd.checkout('002', '40'))

    def test_checkout_if_reached_cd_rental_limit(self):
        d1 = datetime.datetime.now() + timedelta(days=2)
        d2 = datetime.datetime.now() + timedelta(days=3)
        self.assertEqual("Air (001) rented Fantasia 1999 (2) Rental Due: " \
        + d2.strftime("%m/%d/%Y"),\
        self.rent_cd.checkout('001', '2'))
        
        self.assertEqual("Air (001) rented Pride and Prejudice (3)" \
        " Rental Due: " + d2.strftime("%m/%d/%Y"), \
        self.rent_cd.checkout('001', '3'))

        self.assertEqual("Air (001) rented Timeless Songs (4)" \
        " Rental Due: " + d1.strftime("%m/%d/%Y"), \
        self.rent_cd.checkout('001', '4'))

        self.assertEqual('CD rental limit reached', \
        self.rent_cd.checkout('001', '1')) 

    def test_checkout_if_cd_rental_is_overdue(self):
        d1 = datetime.datetime.now() + timedelta(days=2)

        self.assertEqual("Net (002) rented Timeless Songs (4)" \
        " Rental Due: " + d1.strftime("%m/%d/%Y"), \
        self.rent_cd.checkout('002', '4'))

        self.assertEqual('Customer has late rental', \
        self.rent_cd.checkout('002', '3'))
    
