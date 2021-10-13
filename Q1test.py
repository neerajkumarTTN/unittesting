import unittest
from unittest import result
from temperature import convert_far_to_cel , convert_cel_to_far

class TemperatureTests(unittest.TestCase):
    def test_convert_far_to_cels(self):
        self.assertEqual(convert_far_to_cel(72),22.22,
        "result is true")

    def test_convert_cels_to_far(self):
        self.assertEqual(convert_cel_to_far(37),98.60,
        "result is not true")

if __name__=="__main__":
    unittest.main()