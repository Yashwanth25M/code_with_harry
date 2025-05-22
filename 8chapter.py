#    Functions and recursion

# A function can be reused by the programmer in a given program any number of times

# code to add 2 numbers

# a = 2
# b = 3
# c = a + b
# print(c)
# d = 3
# e = 6
# f = d + e
# print(f)

# it can be carried out easily

# def sum(a,b):#function defination
#     return a+b
# a = 2
# b = 3#a and b are parameter
# c = sum(a,b)#function call
# print(c)
# print(sum(3,6))

# Quick Quiz: Write a program to greet a user with “Good day” using functions.

# def greet(name):
#     print(f"Good day {name}")
# name = input("Enter user name:")
# greet(name)

# default parameter value

# def greet(name="stranger"):
#     print(f"Welcome ,{name}")
# greet("Rohan")
# greet()#if parameter is not passed it takes the default value

# Recursion
# a function that calls it self

# def factorial(n):#try  debugging to understand correctly
#     if(n == 1 or n == 0):
#         return 1
#     else:
#         return n*factorial(n-1)
# a=factorial(4)
# print(a)

# The programmer needs to be extremely careful while working with recursion to ensure
# that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most
# direct way to code an algorithm.

# Practice set

# 1. Write a program using functions to find greatest of three numbers.
# def grt(a,b,c):
#     if(a > b and a > c):
#         print(f"{a} is greatest")
#     elif(b > a and b > c):
#         print(f"{b} is greatest")
#     else:
#         print(f"{c} is greatest")
# grt(1,24,9)

# 2. Write a python program using function to convert Celsius to Fahrenheit

# def con(n):
#     print(f"The temperature in fahrenheit is {round(5*(n-32)/9,2)}")
# n=int(input("Enter temperature in celcius: "))
# con(n)

# c=round(3.14183629,2)#syntax   round(value,after point number[in this case two points ])
# print(c)

# 3. How do you prevent a python print() function to print a new line at the end.

# By using end argument

# print("This is start . ",end="")
# print("This is end")

# 4. Write a recursive function to calculate the sum of first n natural numbers

# def sumin(n):
#     if(n == 1 or n == 0):
#         return 1
#     else :
#         return n + sumin(n-1)
# print(sumin(5))

# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

# def pat(n):
#     for i in range(0,n+1):
#         print("*"*(n-i))
# pat(3)

# 6. Write a python function which converts inches to cms.

# def cms(n):
#     return (n*2.54)
# n=int(input("Enter height in inches:"))
# print(f"{n} inches is {cms(n)}cm")

# 7. Write a python function to remove a given word from a list ad strip it at the same time

# def rem(l, word1):
#     return [item for item in l if item != word1]

# def sti(l, word2):
#     return [item.replace(word2, '') for item in l if item != word2]

# l = ["Rohan", "Roopesh", "Ruthvik", "Vishwas"]
# print(rem(l, "Vishwas"))
# print(sti(l, "h"))

# 8. Write a python function to print multiplication table of a given number.

# def mul(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")
# mul(5)