# Newly added features

# Walrus operator(:=)

# if (n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")

# first obtains value of n , then checks with condition

# ADVANCED TYPE HINTS

# from typing import List, Tuple, Dict, Union

# # List of integers
# numbers: List[int] = [1, 2, 3, 4, 5]

# # Tuple of a string and an integer
# person: Tuple[str, int] = ("Alice", 30)

# # Dictionary with string keys and integer values
# scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# # Union type for variables that can hold multiple types
# identifier: Union[int, str] = "ID123"
# identifier = 12345 # Also valid

# These annotations help in making the code self-documenting and allow developers to
# understand the data structures used at a glance.

# MATCH CASE

# similar to switch statement

# A simple program of calculator

# print("CALCULATOR")
# n1 = int(input("Enter a number:"))
# n2 = int(input("Enter a number:"))
# print("""
#       Press 1 for addition
#       Press 2 for subtraction
#       Press 3 for multiplication
#       Press 4 for division
# """)
# act = int(input("Enter your operation:"))
# match act:
#     case 1:
#         print(f"Sum of {n1} and {n2} is {n1+n2}")
#     case 2:
#         print(f"Subtraction of {n1} and {n2} is {n1-n2}")
#     case 3:
#         print(f"Multiplication of {n1} and {n2} is {n1*n2}")
#     case 4:
#         if (n2 != 0 ):
#             print(f"Division of {n1} and {n2} is {n1/n2}")
#         else:
#             print("Please provide valid numbers")
#     case _:
#         print("Unknown error occured")

# DICTIONARY MERGE & UPDATE OPERATORS
# New operators | and |= allow for merging and updating dictionaries.

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged = dict1 | dict2
# print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}


# WITH STATEMENT

# You can now use multiple context managers in a single with statement more cleanly
# using the parenthesised context manager

# with (
# open('file1.txt') as f1,
# open('file2.txt') as f2
# ):

# EXCEPTION HANDLING IN PYTHON
# There are many built-in exceptions which are raised in python when something goes
# wrong.
# Exception in python can be handled using a try statement. The code that handles the
# exception is written in the except clause

# try:
#     a = int(input("Enter a number:"))
#     print(f"You have entered :{a}")

# except Exception as e:
#     print(e)
#     print("You had to enter only number!!")


# handelling a particular type  of error

# print("===  5 COMMON ERRORS ===")

# try:
#     # 1. ValueError
#     num = int(input("Enter a valid integer: "))

#     # 2. ZeroDivisionError
#     print("100 divided by your number is:", 100 / num)

#     # 3. IndexError
#     my_list = [10, 20, 30]
#     print("Accessing element at index 5:", my_list[5])

#     # 4. KeyError
#     my_dict = {"name": "John"}
#     print("Accessing key 'age':", my_dict["age"])

#     # 5. FileNotFoundError
#     with open("nonexistent.txt", "r") as file:
#         data = file.read()

# except ValueError:
#     print("Error: You must enter a valid integer.")

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except IndexError:
#     print("Error: That index is out of range.")

# except KeyError:
#     print("Error: That key doesn't exist in the dictionary.")

# except FileNotFoundError:
#     print("Error: The file you are trying to open does not exist.")

# print("Program completed.")


# RAISING EXCEPTIONS
# We can raise custom exceptions using the ‘raise’ keyword in python.

# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# if(b == 0):
#     raise ZeroDivisionError("Hey dont Enter zero ,it raises zero division error")
# else:
#     print(f"the division of a/b is {a/b}")

# TRY AND FINALLY

# try:
#     a = int(input("Enter a number:"))
#     print(f"You have entered :{a}")

# except Exception as e:
#     print(e)
#     print("You had to enter only number!!")

# else:
#     print("success!!(Entered else)")

# if correct input is provided , it finally reaches  to else part

#TRY WITH FINALLY

# try:
#     a = int(input("Enter a number:"))
#     print(a)
        
# except Exception as e:
#     print(e)

# finally:#finally runs at normal also and also in excepion also
#     print("Inside finally")

# It can be simply written like this

# try:
#     a = int(input("Enter a number:"))
#     print(a)
        
# except Exception as e:
#     print(e)

# print("Inside finally")#now also perform same task like earlier
#but in def function it changes


# def main():
#     try:
#         a = int(input("Enter a number:"))
#         print(a)
        
#     except Exception as e:
#         print(e)

#     print("Inside finally")
# main()#here finally will not execute atleast once also

#usage in def

# def main():
#     try:
#         a = int(input("Enter a number:"))
#         print(a)
        
#     except Exception as e:
#         print(e)

#     finally:
#         print("Inside finally")#executes if try or except runs
# main()


# IF __NAME__== ‘__MAIN__’ IN PYTHON
# ‘__name__’ evaluates to the name of the module in python from where the program is
# ran.
# If the module is being run directly from the command line, the ‘ __name__’ is set to
# string “__main__”. Thus, this behaviour is used to check whether the module is run
# directly or imported to another file.


# open filo.py 

# from filo import myfilo
# #now on running it shows file name

#in simple its used to estimate that weather file ran from original file or imported

# THE GLOBAL KEYWORD
# ‘global’ keyword is used to modify the variable outside of the current scope.

# a = 89
# def fun():
#     global a
#     a = 3
#     print(a)
# fun()
# print(a)

# ENUMERATE FUNCTION IN PYTHON
# The ‘enumerate’ function adds counter to an iterable and returns it

# l = [1 , 2  , 3 , 4 ]
# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1#same task can be performed like
# print("Done tradional way")

# l = [1 , 2  , 3 , 4 ]
# for index ,  item in enumerate(l):
#     print(f"The item number at index {index} is {item}")    

# list comprahension
# l1 = [1 , 2 , 9 ,5 , 3 , 5]#square this list 
# l2 = [item*item for item in l1]
# print(l2)


# practice set 

# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.

# for i in range(1,4):
#     try :
#         with open(f"{i}.txt", 'r') as w:
#             print(f"Reading content of {i}.txt file")
#             print(w.read())

#     except Exception as e:
#         print(f"Error opening {i}.txt ")
#         print(e)

# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function

# l = [i for i in range(0,11)]
# print(f"The original list:{l}")
# for index  , item in enumerate(l):
#     if(index == 2 or index == 4 or index == 6):
#         print(f"The {index}th element is {l[index]}")

# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.

# n = int(input("Enter a number : "))
# l = [n*i for i in range(1,11)]
# print(l)

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

# try :
#     a = int(input("Enter a number:"))
#     b = int(input("Enter a number:"))
#     c = a/b

# except ZeroDivisionError:
#     print(" Handeled ZeroDivisionError , The division of a/b is INFINTE")

# else:
#     print("The division of a/b is",c)

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

# n = int(input("Enter a number : "))
# l = [n*i for i in range(1,11)]
# with open("Tables.txt" , "w") as f:
#     f.write(str(l))