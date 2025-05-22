# variables and datatypes

# a = 30
# b = "abcd"
# c = 3.14
# a,b,c are variables

# different types of data types
# 1.Integers(2,3,4,5)
# 2floating point(1.1,3.45)
# 3.string("abcd","xyz")
# 4.Boolean(True , False)
# 5.None

# RULES FOR CHOOSING AN IDENTIFIER
# • A variable name can contain alphabets, digits, and underscores.
# • A variable name can only start with an alphabet and underscores.
# • A variable name can’t start with a digit.
# • No white space is allowed to be used inside a variable name.


# OPERATORS IN PYTHON
# Following are some common operators in python:
# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.

# type function
# this function returns type of variable
# a = 30
# b = "abcd"
# c = 3.14
# d=True
# print(type(a))#returns integer type
# print(type(b))#returns string type
# print(type(c))#returns floating point
# print(type(d))#returns boolean type

# Type casting
# a = 30 #int to float
# print(f"Before: {type(a)}")
# x=float(a)
# print(f"After: {type(x)}")

# x=3.124 #float to int
# print(type(x))
# y=int(x)
# print(type(y), y)

# f=3 #int to str
# h=str(f)
# print(type(h))

# f=3.13 #float to str
# h=str(f)
# print(type(h))

# d="2" # str to int
# e=int(d)
# print(type(e))

# d="2.11" # str to float
# e=int(d)
# print(type(e))

# Input() function
# It let user provide input 

# simple program to take input of 2 numbers and add them

# a=(input("Enter a number 1:"))
# b=(input("Enter a number 2:"))
# c = a + b
# print(f" The sum of {a} and {b} is {c}") #this performs concatination as it takes input as string

# a=int(input("Enter a number 1:"))
# b=int(input("Enter a number 2:"))
# c = a + b
# print(f" The sum of {a} and {b} is {c}") #this perform sum as it takes input as integer


# practice set

# 1.Write a python program to add two numbers

# a=int(input("Enter a number 1:"))
# b=int(input("Enter a number 2:"))
# c = a + b
# print(f" The sum of {a} and {b} is {c}")

# 2. Write a python program to find remainder when a number is divided by z

# a=int(input("Enter a divider:"))
# b=int(input("Enter a divident:"))
# c = a % b
# print(f" The remainders of {a} is divided by  {b} is {c}")

# 3. Check the type of variable assigned using input () function.

# a=input()
# print(type(a)) # by default take input as string

# 4. Use comparison operator to find out whether ‘a’ given variable 
# a is greater than ‘b’ or not. Take a = 34 and b = 80

# a = 34
# b = 80
# print(f"Is a greater than b : {a>b}")

# 5. Write a python program to find an average of
#  two numbers entered by the user.

# a=int(input("Enter a number 1:"))
# b=int(input("Enter a number 2:"))
# c = (a + b) / 2
# print(f" The average  of {a} and {b} is {c}")

# 6. Write a python program to calculate the 
# square of a number entered by the user.

# a=int(input("Enter a number to find square:"))
# print(f'The square of {a} is {a*a}')