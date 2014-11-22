import unittest
from cd import CD

class TestCD(unittest.TestCase):

    def setUp(self):
        self.cd = CD("1")

    def test_if_object_cd_exists(self):
        self.assertEqual(self.cd.id, "1")

if __name__ == '__Main__':
    unittest.main()      
