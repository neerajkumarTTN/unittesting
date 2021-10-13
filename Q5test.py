import unittest
from Q5 import Car, Point,Employee,Bus

class Q5_test(unittest.TestCase):

    def test_raise_salary(self,):
        emp1=Employee()
        self.assertEqual(emp1.raise_salary(10000),11000,
        "not expected output")

    def test_fare_car(self):
        car1=Car("nano",30,10)
        self.assertEqual(car1.get_fare(),40.15,
        "Not Expected output")
    
    def test_fare_bus(self):
        bus1=Bus("volvo",40,10)
        self.assertEqual(bus1.get_fare(),50.25,
        "Not Expected output")

    def test_point_add(self):
        p1=Point(3,4)
        p2=Point(2,6)
        p3=p1+p2
        self.assertEqual(p3.__repr__(),'(5,10)',
        "not expected result")

if __name__== "__main__":
    unittest.main()