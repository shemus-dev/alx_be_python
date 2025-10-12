class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        

    def follow(self):
        print("lets goo here")
    def __del__(self):
        print("farewell message")

poeple = Person("shem" ,27)
poeple.follow()
        
class Book():
    def __init__(self,title, author ,pages = 0):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__ (self):
        return f"The writer of the book {self.title} is {self.author}"

book1 = Book("The winner Man","Shem Mwendwa")

class Animal():
    def __init__(self,eating ,sleeping):
        self.eating = eating
        self.sleeping = sleeping

    def eat(self):
        print("We love eating")

    def sleep(self):
        print("We love sleeping")
class Dog(Animal):
    def __init__(self, eating, sleeping,breed = 0, color=0):
        super().__init__(eating, sleeping)
        self.breed = breed
        self.color = color

    def bark(self):
        print("They are barking")

Doogged = Dog("buddy","bazzlingg")
Doogged.bark()
Doogged.eat()

# Multilevel Inheritance :A child class inherits from multiple parent classes

class Flyer:
  def fly(self):
    print("Flying...")

class Swimmer:
  def swim(self):
    print("Swimming...")

class Duck(Flyer, Swimmer):
  pass

duck = Duck()
duck.fly()  # Output: Flying..
duck.swim()  # Output: Swimming..

#polymorphosm 
class Duck:
    def swim(self):
        print("The duck is swimming")

    def fly(self):
        print("The duck is flying")

class Swan:
    def swim(self):
        print("The swan is swimming")

    def fly(self):
        print("The swan is flying")

birds = [Duck(),Swan()]

for bird in birds:
    bird.swim()
    bird.fly()

#class variable = is a variable that is shared by all objects (instances) of a class.
#It is defined inside the class, but outside any instance methods (__init__

class Car:
    wheels = 0
    def __init__(self,color,barnd):
        self.color = color
        self.barnd = barnd
        Car.wheels += 1

car1 = Car("blue","jeep")
car2 = Car("red","benzz")

print(Car.wheels)



        
        