import unittest
from customer import Customer

class TestCust(unittest.TestCase):
    
    def setUp (self):
        self.cust = Customer("001", "James")

    def test_if_customer_object_exists (self):
        self.assertEqual(self.cust.name, "James")
