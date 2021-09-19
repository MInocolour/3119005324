import unittest
from main_for_test import main_test


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main_test(),0.99)


if __name__ == '__main__':
    unittest.main()
