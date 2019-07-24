#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Programming Exercises 1 - 10

https://github.com/rednikon/Python-programming-exercises

@author: veemac
"""

# COMPLETE 1 - 5 BY FRIDAY JULY 12

# Question 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# My answer: use the range function to find the applicable numbers, and present them as a list 
l = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print(',',str(l))


# Question 2:
# Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line.
# My answer: create a recursive function to find the factorial.
def factorial(x):
    """A recursive function to find the factorial of a user-generated integer"""
    if x == 0:
        return 1
    return x * factorial(x - 1)
    
x = int(input("Enter a number for the factorial equation: "))
print(factorial(x))


# Question 3: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number
# between 1 and n (both included) and then the program should print the dictionary.
# My answer: create a dictionary using the dict() function, and fill it based on user input
squares = dict()
base = int(input("Enter a number to create a dictionary of squares: "))

for i in range(1, base +1):
    squares[i] = i*i
    
print(squares)


# Question 4: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# My answer: accept comma-separated numbers from the user, convert the string to integers, and build a list and tuple out of it

q5_numbers = input("Enter a comma-separated list of numbers: ")
q5_list = q5_numbers.split(',')
q5_tuple = tuple(q5_list)
print(q5_list)
print(q5_tuple)


# Question 5:
