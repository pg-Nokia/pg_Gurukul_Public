##Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?
# class car():
#     brand = "renault"
#     model = "duster"
#     year = 2020
# print(car.brand)
# print(car.model)
# print(car.year)
import math
from time import sleep


##Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?
# class students():
#     def __init__(self,name, rollnumber, marks):
#         self.name = name
#         self.rollnumber = rollnumber
#         self.marks = marks
#
#     def display_info(self):
#         print(f"Student name: {self.name}")
#         print(f"Student Roll number: {self.rollnumber}")
#         print(f"Student Marks: {self.marks}")
#
# s1 = students("Joseph", 123 , 99)
# s2 =  students("Jeena", 1234, 99)
# s1.display_info()
# s2.display_info()

##Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?
# class rectangle():
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def display_area(self):
#         return self.length*self.width
#     def display_perimeter(self):
#         return 2*(self.length+self.width)
#     def display_info(self):
#         print("Method 1")
#         print(f"Area of the rectangle: {s1.display_area()}")
#         print(f"perimeter of the rectangle: {s1.display_perimeter()}")
# s1 = rectangle(20,40)
# s1.display_info()
# print("Method 2")
# print(f"Area of the rectangle : {s1.display_area()}")
# print(f"Perimeter of the rectangle : {s1.display_perimeter()}")

##Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?
#
# class circle():
#     def __init__(self,radius):
#         self.radius =  radius
#     def getarea(self):
#         return math.pi*self.radius**2
#     def getcircumference(self):
#         return 2*math.pi*self.radius
#     def display_info(self):
#         print(f"Area of the circle : {c1.getarea()}")
#         print(f"Circumference of the circle : {c1.getcircumference()}")
#
# c1 = circle(5)
# c1.display_info()

##Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

# class account:
#     def __init__(self,debit,credit,acc_no):
#         self.debit = debit
#         self.credit = credit
#         self.acc_no = acc_no
#     def balance(self):
#         return self.credit-self.debit
#     def display_info(self):
#         print(f"The balance in account no {self.acc_no} is {acc.balance()}")
# acc = account(1000,10000,78912345)
# acc.display_info()

##Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.
# class employee:
#     current_employee = 1
#     def __init__(self,name):
#         self.name = name
#         employee.increment_employee()
#     @classmethod
#     def increment_employee(cls):
#         employee.current_employee += 1
#     @classmethod
#     def display_info(cls):
#         print(f"Total employee is : {employee.current_employee}")
# emp1 = employee("Joseph")
# emp1.display_info()
#
# emp2 = employee("Jeena")
# emp2.display_info()

##Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method.
# class book:
#     def __init__(self,title,author,price=30):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display_info(self):
#         print(f"Author of the book {self.title} is {self.author} and the cost is {self.price}")
# book1 = book("Ghost","Joseph")
# book1.display_info()
#
# book2 = book("Gods Own country","Jeena")
# book2.display_info()

##Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.
# class temperature:
#     def __init__(self,celsius):
#         self.celsius = celsius
#     def temperature_convert_fahrenheit(self):
#         return self.celsius * (9/5) +32
#     def display_info(self):
#         fahrenheit = self.temperature_convert_fahrenheit()
#         print(f"Fafrenheit of the celsius {self.celsius} is : {fahrenheit}")
# temp1 = temperature(98)
# temp1.display_info()
#
# temp2 = temperature(97)
# temp2.display_info()

##Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum
# class time:
#     current_hour = 3
#     current_min = 30
#     def __init__(self,hour,min):
#         self.hour = hour
#         self.min = min
#     def add_hour(self):
#         return self.hour + time.current_hour
#     def add_min(self):
#         return self.min + time.current_min
#     def display_info(self):
#         final_hour = self.add_hour()
#         final_min = self.add_min()
#         print(f"Hour is {final_hour} and min is {final_min}")
# hour1 = time(12,0)
# hour1.display_info()
#
# hour2 = time(9,18)
# hour2.display_info()

##Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method set_bonus_percentage() to change the bonus percentage for all employees. Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee

class employeesalary():
    def __init__(self,name,basic_salary,bonus_percentage):
        self.basic_salary = basic_salary
        self.bonus_percentage = bonus_percentage
        self.name = name
    def set_bonus_percentage(self):
        bonus_amount = (self.basic_salary*self.bonus_percentage)/100
        total_salary = self.basic_salary+bonus_amount
        return total_salary
    def display_info(self):
        print(f"Total salary of the {self.name} : {self.set_bonus_percentage()}")
    @classmethod
    def display_all_info(cls,employee_list):
        for employee in employee_list:
            employee.display_info()

emp1 = employeesalary("emp1",1000,10)
emp2 = employeesalary("emp2",2000,20)
employeesalary.display_all_info([emp1,emp2])