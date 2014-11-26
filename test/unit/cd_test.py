import unittest
from cd import CD

class TestCD(unittest.TestCase):

    def setUp(self):
        self.cd = CD("1", "Twila Paris Hits", "No", 2)

    def test_if_object_cd_exists(self):
        self.assertEqual(self.cd.title, "Twila Paris Hits")

    def test_if_cd_is_not_rented(self):
        self.assertEqual(self.cd.rented, "No")

if __name__ == '__Main__':
    unittest.main()      
