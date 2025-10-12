class Car:
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #default reading

    def getdescription(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name
    def readometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def updateredometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementodometer(self,miles):
        self.odometer_reading +=miles
        return self.odometer_reading


mycar = Car("Toyota", "Camry", 2020)
print(mycar.getdescription())
print(mycar)
mycar.readometer()
mycar.updateredometer(200)
x =mycar.incrementodometer(50)
print(x)

class Product():
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def seeproduct(self):
        # print(f"{self.name} {self.price} {self.quantity}")
        return f"Product: {self.name}, Price: {self.price} ,Quantity: {self.quantity}"

    def totalproduct(self):
        x = self.price * self.quantity
        print(x)

product1= Product("Ushindi",200, 3)
print(product1.seeproduct())
print(product1.totalproduct())
products = [

    Product("ajje",100, 3),
    Product("UshDetollindi",400, 3),
    Product("Geyshar",600, 3),
]

for p in products:
    print(p.seeproduct())


class Point:
    def __init__(self,x,y):
         self.x = x
         self.y = y
point = Point(3,4)
print(f"Point coordinates: ({point.x}, {point.y})")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(person)  

# class Filehandler:
#     def __init__(self,filename):
#         self.filename = filename
#         try:
#             self.file = open(filename,"r")
#         except:
#             print(f"{filename} is not found")

#     def read_data(self):
#         return self.file.read()
    
#     def __del__(self):
#         self.file.close()
        
# fileobject = Filehandler("sample.txt")
# print(fileobject.read_data())


#inheritance 
# By using the super() function, you do not have to use the name of the parent element, it will 
# automatically inherit the methods and properties from its parent.

class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
   def __init__(self, name,breed):
      super().__init__(name)
      self.breed = breed

   def make_sound(self):
      print(f"here is {self.name} {self.breed}")
   
dog = Dog("buddy","hiil")
dog.make_sound()
   



