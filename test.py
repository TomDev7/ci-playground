import unittest

print("test")

class TestClass(unittest.TestCase):

    def test_addition(self):

        self.assertEqual(1 + 2 == 3)

    def test_multiplication(self):

        self.assertEqual(2 * 3 == 6)

if __name__ == '__main__':
    unittest.main()
