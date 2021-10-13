import unittest
from Q2 import sum
class sumTests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(123),6)
if __name__=="__main__":
    unittest.main()