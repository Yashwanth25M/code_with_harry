# Condition Expression

# Quick Quiz: Write a program to print yes when the age entered by the user is greater
# than or equal to 18.

# age = int(input("Enter your age :"))
# if(age >= 18):
#     print("You are above age of consent")
# else:
#     print("You are not above age of consent")    

# RELATIONAL OPERATORS
# Relational Operators are used to evaluate conditions inside the if statements. Some
# examples of relational operators are:
# ==: equals.
# > =: greater than/ equal to.
# < =: lesser than/ equal to.

# LOGICAL OPERATORS
# In python logical operators operate on conditional statements. For Example:
# • and – true if both operands are true else false.
# • or – true if at least one operand is true or else false.
# • not – inverts true to false & false to true.

#     AND              OR            NOT
# 0 0  0          0 0  0          0   1
# 1 1  1          1 1  1          1   0
# 0 1  0          0 1  1
# 1 0  0          1 0  1        


# IMPORTANT NOTES:
# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail.



# Practise set
# 1. Write a program to find the greatest of four numbers entered by the user.

# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1:", a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2:", a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Greatest number is a3:", a3)

# elif(a4>a1 and a4>a2 and a4>a3):
#     print("Greatest number is a4:", a4)

# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# marks1 = int(input("Enter Marks 1: "))
# marks2 = int(input("Enter Marks 2: "))
# marks3 = int(input("Enter Marks 3: "))

# # Check for total percentage
# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed:", total_percentage)

# else:
#     print("You failed, try again next year:", total_percentage)

# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# p1 = "Make a lot of money"
# p2 = "buy now"  
# p3 = "subscribe this"  
# p4 = "click this"

# message = input("Enter your comment: ")

# if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
#     print("This comment is a spam")

# else:
#     print("This comment is not a spam")

# spam = [ "make a lot of money", "buy now", "subscribe this", "click this"]
# cmt = input("Comment:")
# lo=cmt.lower()
# if (lo  in spam ):
#     print("Spam detected")
# else:
#     print("no spam message")

# 4. Write a program to find whether a given username contains less than 10
# characters or not.

# username = input("Enter username: ")

# if(len(username)<10):
#     print("Your username contains less than 10 characters")
# else:
#     print("Your username contains more than or equal to 10 characters")

# 5. Write a program which finds out whether a given name is present in a list or not.

# l = ["Harry", "Rohan", "Shubham", "Divya"]

# name = input("Enter your name: ")

# if(name in l):
#     print("Your name is in the list")
# else:
#     print("Your name is not in the list")

# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# marks = int(input("Enter your marks: "))

# if(marks<=100 and marks>=90):
#     grade = "Ex"
# elif(marks<90 and marks>=80):
#     grade = "A"
# elif(marks<80 and marks>=70):
#     grade = "B"
# elif(marks<70 and marks>=60):
#     grade = "C"
# elif(marks<60 and marks>=50):
#     grade = "D"
# elif(marks<50):
#     grade = "F"

# print("Your grade is:", grade)

# 7. Write a program to find out whether a given post is talking about “Harry” or not.

# post = input("Enter the post: ")

# if("harry" in post.lower()):
#     print("This post is talking about harry")
# else:
#     print("This post is not talking about harry")