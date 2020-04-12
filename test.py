import unittest

class TestClass(unittest.TestCase):

    def setUp(self):
        print ('setting up tests')

    def test_addition(self):

        print('add')
        self.assertEqual(1 + 2, 3)

    def test_multiplication(self):

        print('multiply')
        self.assertEqual(2 * 3, 8)

    def test_division(self):

        print('divide')
        self.assertEqual(4 / 2, 2)

    def tearDown(self):
        print ('tearing down tests')

if __name__ == '__main__':
    unittest.main()
