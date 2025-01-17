from audioop import reverse
from http.cookiejar import uppercase_escaped_char
from idlelib.debugger_r import restart_subprocess_debugger
from itertools import count
from unittest import removeResult

##Write a Python function to find the maximum of three numbers
numbers = (10,20,100)
print("Maximum of 3 number is :",max(numbers))

##Write a Python function to multiply all the numbers in a list.
# def number_list(mylist):
#     result = 1
#     for i in mylist:
#         result = result * i
#     return result
# mylist = [8, 2, 3, -1, 7]
# print(number_list(mylist))

##Write a Python program to reverse a string.
# def reverse_string(name):
#     return name [::-1]
# print(reverse_string(name="1234abcd"))

##Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     else:
#         result = 1
#         for i in range(1, n+1):
#             result *= i
#         return result
# # Get user input
# num = 5
# print(f"The factorial of {num} is: {factorial(num)}")
# print()

##Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# def get_distinct_elements(input_list):
#     # Use a set to get unique elements and convert it back to a list
#     distinct_elements = list(set(input_list))
#     return distinct_elements
# list = get_distinct_elements(input_list=[1,2,3,3,3,3,4,5])
# print("The distinct element from the list is :",list)

##Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# def is_prime(n):
#     """Check if a number is prime."""
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1): ## 2, 1+1
#         if n % i == 0:
#             return False
#     return True
#
# number = int(input("Enter a number to check if it's prime: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

##Write a Python program to print the even numbers from a given list.
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in list:
#     if i % 2 ==0:
#         print(i)

##Write a Python function that accepts a string and counts the number of upper and lower case letters.
# def count_case_letters(s):
#     """Count uppercase and lowercase letters in a string."""
#     upper_count = 0
#     lower_count = 0
#
#     for char in s:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#
#     return upper_count, lower_count
#
#
# # Example usage
# input_string = input("Enter a string: ")
# upper_count, lower_count = count_case_letters(input_string)
# print(f"Uppercase letters: {upper_count}")
# print(f"Lowercase letters: {lower_count}")

##Write a Python function to sum all the numbers in a list.
# def number_list(mylist):
#     result = 0
#     for i in mylist:
#         result = result + i
#     return result
# mylist = [8, 2, 3, 0, 7]
# print(number_list(mylist))


##Write a Python function that checks whether a passed string is a palindrome or not.
# def is_palindrome(s):
#     # Remove any spaces and convert the string to lowercase
#     s = s.replace(" ", "").lower()
#
#     # Check if the string is equal to its reverse
#     return s == s[::-1]
#
# string = "A man a plan a canal Panama"
# if is_palindrome(string):
#     print(f'"{string}" is a palindrome.')
# else:
#     print(f'"{string}" is not a palindrome.')
#
