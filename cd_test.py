import unittest
from cd import CD

class TestCD(unittest.TestCase):

    def setUp(self):
        self.cd = CD()

    def test_add_cd(self):
        cd = CD("1")
        self.assertEqual(cd, "1")

if __name__ == '__Main__':
    unittest.main()      
