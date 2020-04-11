import unittest

class TestClass(unittest.TestCase):

    def setUp(self):
        print ('setting up tests')

    def test_addition(self):

        self.assertEqual(1 + 2 == 3)

    def test_multiplication(self):

        self.assertEqual(2 * 3 == 6)

    def tearDown(self):
        print ('tearing down tests')

if __name__ == '__main__':
    unittest.main()
