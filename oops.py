'''
#Object and Class
A class is a blueprint or template for creating objects. It defines a set of attributes (data members) and methods (functions) 
that the objects created from the class will have.

An object is an instance of a class. It is a concrete realization of the class blueprint and 
represents a specific entity or concept in your program.

---Real time applications---
In a banking application, the Account class can represent customer accounts. 
Each customer's account is an instance (object) of this class.

1.
class Bike:
    name=""
    range=0

bike1=Bike()

Bike.name="Yamaha"
Bike.range="150km/hr"

print(Bike.name)
print(Bike.range)

#by using __init__ constructer

class Bike:
    def __init__(self,name,range):
        self.name=name 
        self.range=range 

bike1=Bike("Yamaha","150k/hr")
print(bike1.name)
print(bike1.range)

#example of demonstrates a bankaccount for more understanding of __init__

class BankAccount:
    def __init__(self,accountNumber,balance):
        self.accountNumber=accountNumber
        self.balance=balance
    
    def deposite(self,amount):
        self.balance+=amount 
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount 
        else:
            print("Insufficient Amount")

A=BankAccount("00001",6000)
B=BankAccount("00002",10000)

A.deposite(int(input()))
B.withdraw(int(input()))

print(A.balance)
print(B.balance)


2.
#Inheritance 
 Inheritance is the capability of one class to derive or inherit the properties from another class. 
 The class that derives properties is called the derived class or child class and the class from 
 which the properties are being derived is called the base class or parent class.

---Real time applications---
In a game development framework, you might have a base class "GameObject" representing common game objects 
like characters and obstacles. Subclasses like PlayerCharacter and Enemy inherit attributes and methods from 
the GameObject class while adding their specific functionality.
 
class Person:
    def __init__(self,name,IdNumber):
        self.name=name
        self.IdNumber=IdNumber 

    def display(self):
        print("I am {}".format(self.name))
        print("My IdNumber:{}".format(self.IdNumber))


    def details(self):
        print(self.name)
        print(self.IdNumber)

class Employee(Person):
    def __init__(self,name,IdNumber,branch,college):
        self.branch=branch
        self.college=college 

        Person.__init__(self,name,IdNumber)

    def details(self):
        print("Branch :{}".format(self.branch))
        print("College: {}".format(self.college))

A=Employee('Rashmitha',"O170006","ECE","RGUKT")

A.display()
A.details()


In Python, the super() function is used to call methods 
and access attributes from the parent or superclass within a subclass. 
It's particularly useful in situations where you want to extend the 
functionality of a method inherited from the superclass while still using the 
implementation provided by the superclass.


class Vehicle:
    def __init__(self,make,model):
        self.make=make 
        self.model=model 
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type=fuel_type
    def info(self):
        return f"{super().info()},fuel_Type:{self.fuel_type}"
    
class Bike(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type=fuel_type
    def info(self):
        return f"{super().info()},fuel_Type:{self.fuel_type}"
        

A=Car("Toyota","Camry","Gaslione")
B=Bike("Yamaha","Mountain Bike","Off-road")
print(A.info())
print(B.info())


3.
#Encapsulation 
Encapsulation is a fundamental concept in object-oriented programming (OOP) that 
involves bundling the data (attributes) and the methods (functions) that
operate on that data into a single unit called an "object."


---Real time applications---
In a medical records system, patient information is encapsulated within the Patient class. 
Access to this information is controlled through methods like 
getAge() and setDiagnosis(), ensuring data security and integrity

class Student:
    def __init__(self, name, age):
        self._name = name 
        self._age = age  

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name:
            self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age

student = Student("Alice", 25)

print("Student Name:", student.get_name())
print("Student Age:", student.get_age())

# Modifying attributes through public methods
student.set_name("Bob")
student.set_age(26)
print("Updated Student Name:", student.get_name())
print("Updated Student Age:", student.get_age())

4.
#polymorphism 

Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects 
of different classes to be treated as objects of a common superclass. 
It enables you to write more generic and flexible code by abstracting the specific details of classes and their methods.
The term "polymorphism" comes from Greek, where "poly" means "many," and "morph" means "form," 
indicating the ability of objects to take on multiple forms.

---Real time applications---
In a drawing application, various shapes like circles, rectangles, and triangles can 
all implement a common interface with a draw method. This allows the user to 
interact with and draw different shapes using the same tools.


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)

shapes = [circle, rectangle]

for shape in shapes:
    print("Area:", shape.area())

5.Data Abstraction

Data abstraction is a fundamental concept in programming that involves simplifying complex systems or 
objects by creating models that focus on the essential aspects while hiding unnecessary details. 
It allows us to interact with these systems or objects 
through well-defined interfaces, making it easier to work with them and maintain code.

---Real time applications---
In a car navigation system, the GPS module abstracts complex geographic data. Users interact 
with the system through high-level commands like "Navigate to [destination]" without needing to 
understand the details of GPS coordinates and map algorithms.

class TVRemote:
    def __init__(self, tv):
        self.tv = tv  # The TV object that we're abstracting

    def turn_on(self):
        self.tv.power = True
        print("TV is on")

    def turn_off(self):
        self.tv.power = False
        print("TV is off")

    def change_channel(self, channel):
        if self.tv.power:
            self.tv.channel = channel
            print(f"Changed to channel {channel}")
        else:
            print("TV is off, please turn it on first")

class TV:
    def __init__(self):
        self.power = False
        self.channel = 1


my_tv = TV()
my_remote = TVRemote(my_tv)


my_remote.turn_on()
my_remote.change_channel(5)
my_remote.turn_off()
'''