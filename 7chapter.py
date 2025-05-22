# # Loops

# # To print number from 1 to 5
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# # saame thing can be done by 
# for i in range(1,6):
#     print(i)

# Types of loops 
# -while loop
# -for loop

# While loop
# syntax
# while(condition):
    # code
# while loops execute only when condition is true

# to carry out above code to print from 1 to 5

# i=1
# while(i<6):
#     print(i)
#     i += 1

# Quick Quiz: Write a program to print 1 to 50 using a while loop.

# i = 1
# while(i<51):
#     print(i)
#     i += 1

# Quick Quiz: Write a program to print the content of a list using while loops.

# l = ["ram" , "raghu" , "ramesh" , "abhi"]
# i = 0
# while( i < len(l)):
#     print(f"{l[i]}")
#     i += 1

# for loop

# for i in range(1,51):
#     print(i)#num from 1 to 50

# l = ["ram" , "raghu" , "ramesh" , "abhi"]
# for i in l:
#     print(i)

# range function with step-size
# for i in range(0,50,2):
    # print(i)

# s = "abcdefgh"#for loop with string
# for i in s:
#     print(i)

# s = ("a" , "b" ,"c" , "d" , "e" , "f" , "g" , "h")#for loop with tuple
# for i in s:
#     print(i)

# s = ["a" , "b" ,"c" , "d" , "e" , "f" , "g" , "h"]#for loop with list
# for i in s:
#     print(i)


# for loop with else

# l= [1,7,8]
# for item in l:
#     print(item)
# else:
#     print("done") # this is printed when the loop exhausts!

# Else only executes when complete for loop executes


# Break statement
# ‘break’ is used to come out of the loop when encountered. It instructs the 
# program to –exit the loop now.

# for i in range(1,5):
#     if(i == 3):
#         break#at i=3 whole loop exit
#     print(i)

# continue statement

# ‘continue’ is used to stop the current iteration of the loop and continue 
# with the next one. It instructs the Program to “skip this iteration”.

# for i in range(1,5):
#     if(i == 3):
#         continue #at i=3 skip the iteration
#     print(i)

# Pass statement
# pass is a null statement in python.
# It instructs to “do nothing”.

# l = [1,7,8]
# for item in l:
#     pass # without pass, the program will throw an error

# Practice set

# 1. Write a program to print multiplication table of a given number using for loop.

# n = int(input("Enter a number :"))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

# 2. Write a program to greet all the person names stored in
#  a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for i in l:
#     if(i.startswith("S")):
#         print(f"Hello {i}")

# 3. Attempt problem 1 using while loop

# n = int(input("Enter a number :"))
# i = 0
# while (i < 11):
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# 4. Write a program to find whether a given number is prime or not

# n = int(input("Enter a number:"))
# for i in range(2,n):
#     if ( n % i == 0):
#         print(f"{n} is not a prime number")
#         break
# else:
#     print(f"{n} is  a prime number")       

# 5. Write a program to find the sum of first n natural numbers using while loop.

# n = int(input("Enter a number:"))
# l = 0 
# for i in range (0,n+1):
#     l += i
# print(f"The sum of first {n} numbers is {l}")

# 6. Write a program to calculate the factorial of a given number using for loop.

# l = 1
# n = int(input("Enter a number:"))
# for i  in range (1,n+1):
#     l *= i
# print(f"The factorial of {n} is {l}")

# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3 
 
# n = int(input("Enter a number:"))
# for i in range (1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

"""
    *
   ***
  *****
 *******
*********
"""






# Pending all star pattern










































# # 10. Write a program to print multiplication table of n using for loops in reversed order.
# m=1
# n = int(input("Enter number"))
# for i in range(0,11):
#     m = 10 - i
#     if(m == 0):
#         break
#     print(f"{n} X {m} = {m*n}")