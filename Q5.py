class Employee:
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
       # self.email_id=first_name+"."+last_name+"@tothenew.com"
    @property
    def email_id(self):
        email=f"{self.first_name}{self.last_name}@tothenew.com"
        return email
emp1=Employee("neeraj","kumar",1200)
emp2=Employee("ajay","singh",2500)
print(emp1.email_id)
print(emp2.email_id)

class Employee:
    raise_percentage=10
    def __init__(self):
        pass
        
    def raise_salary(self,salary):
        self.salary=salary
        self.salary=(self.salary+(self.salary)*self.raise_percentage/100)
        return self.salary
emp1=Employee()
print(emp1.raise_salary(10000))

class Vehicle:
     def __init__(self,make,mileage,capacity):
         self.make=make
         self.mileage=mileage
         self.capacity=capacity

     def get_fare(self):
        print("fare of parent class")
        raise NotImplementedError("must implement get fare method")
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


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self) ->str:
        return f"({self.x},{self.y})"
    def __add__(self,Point2):
        if(isinstance(Point2,Point)):
            a=self.x+Point2.x
            b=self.y+Point2.y
            return (Point(a,b))
        else:
            return "Unsupported data"
p1=Point(3,4)
p2=Point(2,6)
p3=p1+p2
print(p3)
