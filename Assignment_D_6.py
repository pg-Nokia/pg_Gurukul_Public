# # Assignment 1: Static Methods
# # Create a class MathOperations that contains:
# # A static method add_numbers that takes two arguments and returns their sum.
# # A static method multiply_numbers that takes two arguments and returns their product.
#
# class MathOperations:
#     @staticmethod
#     def add_numbers(a,b):
#         return a+b
#
#     @staticmethod
#     def multiply_numbers(a, b):
#         return a * b
# result_Add=MathOperations.add_numbers(5,8)
# result_multiply=MathOperations.multiply_numbers(5,8)
# print(f"Sum :{result_Add}")#add_numbers(a, b): Takes two arguments and returns their sum.
# print(f"Product :{result_multiply}")#multiply_numbers(a, b): Takes two arguments and returns their product.


# Assignment 2: Class Methods
# Create a class Person that keeps track of the number of people created. The class should have:
# A class variable count to count instances of the class.
# A class method get_count that returns the current count.

# class Person:
#     count=0  # Class variable to keep track of the number of instances
#     def __init__(self):
#         Person.count+=1 # Increment count when a new instance is created
#     @classmethod
#     def get_count(cls):
#         return cls.count # Return the current value of the count
# person1 = Person()
# person2 = Person()
# person3 = Person()
# # Getting the current count of people created
# print(f"Number of people created: {Person.get_count()}")  # Output: Number of people created: 3

#
# Assignment 3: Using Both Static and Class Methods
# Create a class TemperatureConverter with the following:
# A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
# A class method info that returns a message about temperature conversions.


# class TemperatureConverter:
#     @staticmethod
#     def Celsius_to_Fahrenheit(Celsius):
#         return (Celsius*9/5)+32
#
#     @classmethod
#     def info(cls):
#         return "This class provides methods for temperature conversions between Celsius and Fahrenheit."
# # Using the static method to convert Celsius to Fahrenheit
# temp_in_fahrenheit =TemperatureConverter.Celsius_to_Fahrenheit(25)
# print(f"25°C in Fahrenheit is: {temp_in_fahrenheit}°F")  # Output: 25°C in Fahrenheit is: 77.0°F
# message = TemperatureConverter.info()
# print(message)# Output: This class provides methods for temperature conversions between Celsius and Fahrenheit.

# #Assignment 4: Single Inheritance
# Create two classes:
# Animal with a method sound that prints "Animal sound".
# Dog that inherits from Animal and overrides the sound method to print "Bark".

# class Animal:
#     def sound(self):
#         print("Animal Sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# # Creating an instance of Animal and calling sound method
# animal =Animal()
# animal.sound()# Output: Animal sound
# # Creating an instance of Dog (which inherits from Animal) and calling sound method
# dog = Dog()
# dog.sound()  # Output: Bark

# Assignment 5: Multiple Inheritance
# Create two classes:
# Bird with a method fly that prints "Flying".
# Fish with a method swim that prints "Swimming".
# A class Duck that inherits from both Bird and Fish.

# class Bird:
#     def fly(self):
#         print("Flying")
# class Fish:
#     def swim(self):
#         print("Swimming")
# class Duck(Bird,Fish):
#     pass
# # Creating an instance of Duck
# duck = Duck()
#
# # Duck can both fly and swim because it inherits from both Bird and Fish
# duck.fly()   # Output: Flying
# duck.swim()  # Output: Swimming
#
# Assignment 6: Abstract Class
# Use the abc module to create an abstract class Shape that contains:
# An abstract method area().
# Two concrete classes Circle and Rectangle that inherit from Shape and implement the area method.
#
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     # Creating an instance of Circle and calculating the area
# circle = Circle(5)
# print(f"Area of the circle: {circle.area():.2f}")  # Output: Area of the circle: 78.54
#
#     # Creating an instance of Rectangle and calculating the area
# rectangle = Rectangle(4, 6)
# print(f"Area of the rectangle: {rectangle.area()}")  # Output: Area of the rectangle: 24


# Assignment 7: Encapsulation
# Create a class BankAccount that uses encapsulation:
# Private attributes _balance.
# Public methods deposit() and withdraw() that modify _balance safely.
#
# class BankAccount:
#     def __init__(self,initial_balance=0):
#         self._balance = initial_balance  # Private attribute
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrew: {amount}")
#         else:
#             print("Insufficient balance or invalid amount.")
#
#     def get_balance(self):
#         return self._balance
# # Creating an instance of BankAccount with an initial balance of 100
# account =BankAccount(100)
#
# # Depositing money into the account
# account.deposit(50) # Output: Deposited: 50
#
# # Withdrawing money from the account
# account.withdraw(30) # Output: Withdrew: 30
#
# # Trying to withdraw more than the available balance
# account.withdraw(200)  # Output: Insufficient balance or invalid amount.
#
# # Checking the balance
# print(f"Current balance: {account.get_balance()}")  # Output: Current balance: 120



# Assignment 8: Polymorphism with Method Overriding
# Create two classes Cat and Dog with a method speak().
# The Dog class should implement speak() to print "Woof".
# The Cat class should implement speak() to print "Meow".
#
# class Dog:
#     def speak(self):
#         print("Woof")
#
# class Cat:
#     def speak(self):
#         print("Meow")
# # Creating instances of Dog and Cat
# dog = Dog()
# cat = Cat()
#
# # Calling the speak method on both instances
# dog.speak()  # Output: Woof
# cat.speak()  # Output: Meow



# Assignment 9: Polymorphism with Method Overloading
# Create a class Calculator with a method add() that:
# Can accept 2 or 3 arguments and returns their sum.
# Hint: Use default parameters to handle method overloading in Python.
#
# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
# calc = Calculator()
#
# # Adding two numbers
# result_two_args = calc.add(10, 20)
# print(f"Sum of 10 and 20: {result_two_args}")  # Output: Sum of 10 and 20: 30
#
# # Adding three numbers
# result_three_args = calc.add(10, 20, 30)
# print(f"Sum of 10, 20 and 30: {result_three_args}")  # Output: Sum of 10, 20 and 30: 60



# Assignment 10: Multilevel Inheritance
# Create three classes:
# LivingBeing with a method breathe() that prints "Breathing".
# Mammal that inherits from LivingBeing and adds a method walk() that prints "Walking".
# Human that inherits from Mammal and adds a method think() that prints "Thinking".


class LivingBeing:
    def breathe(self):
        print("Breathing")

class Mammal(LivingBeing):
    def walk(self):
        print("Walking")

class Human(Mammal):
    def think(self):
        print("Thinking")
# Creating an instance of Human
human = Human()

# Calling methods from Human, Mammal, and LivingBeing
human.breathe()  # Output: Breathing (from LivingBeing)
human.walk()     # Output: Walking (from Mammal)
human.think()    # Output: Thinking (from Human)
