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
