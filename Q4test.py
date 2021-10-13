import unittest
from Q4 import Car,Bus
class Test(unittest.TestCase):
    def test_get_fare(self):
        car1=Car("nano",30,10)
        self.assertEqual(car1.get_fare(),40.15)

    def test_get_fare(self):
        bus1=Bus("Volvo",40,10)
        self.assertEqual(bus1.get_fare(),50.25)


if __name__=="__main__":
    unittest.main()