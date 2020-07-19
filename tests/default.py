import unittest

class Tester(unittest.TestCase):
    def test_default(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Sum is 6.")

if __name__ == '__main__':
    unittest.main()