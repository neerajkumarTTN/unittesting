class Vehicle:
     def __init__(self,make,mileage,capacity):
         self.make=make
         self.mileage=mileage
         self.capacity=capacity

     #def get_fare(self):
        #print("fare of parent class")
       # raise NotImplementedError("must implement get fare method")
#class Scooter(Vehicle):
    #def __init__(self,make,mileage,capacity):
        #Vehicle.__init__(self,make,mileage,capacity)
#obj1=Scooter("abc",40,15)

class Car(Vehicle):
    def __init__(self,make,mileage,capacity):
        Vehicle.__init__(self,make,mileage,capacity)

    def get_fare(self):
        fare_car=(self.capacity+self.mileage)+15/100
        return fare_car

class Bus(Vehicle):
    def __init__(self,make,mileage,capacity):
        Vehicle.__init__(self,make,mileage,capacity)
    def get_fare(self):
       fare_bus=(self.capacity+self.mileage)+25/100
       return fare_bus
#print(obj1.get_fare())
bus1=Bus("volvo",40,10)
car1=Car("nano",30,10)
print("Fare of bus1 is :",bus1.get_fare())
print("Fare of car1 is:",car1.get_fare())