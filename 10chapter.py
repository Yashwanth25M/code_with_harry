# Object oriented programming

# A class is a blueprint for creating object
# An object is an instantiation of a class

# class Employee:
#     name = "harish"#attributes
#     language = "kannada"
#     salary = 1000000

# trainer1 = Employee()
# print(trainer1.name , trainer1.language , trainer1.salary)#method

# INSTANCE ATTRIBUTES

# class Employee:
#     name = "harish"#attributes
#     language = "kannada"
#     salary = 1000000

# trainer2 = Employee()
# trainer2.name = "Ganesha"#instance attributes
# trainer2.salary = 10000
# print(trainer2.name , trainer2.language , trainer2.salary)
# trainer3 = Employee()
# print(trainer3.name , trainer3.language , trainer3.salary)

# here name and salary are instance attributes , where language is class attribute
# Instance attributes, take preference over class attributes during assignment & retrieval.

# SELF PARAMETER

# class Employee:
#     name = "harish"#attributes
#     language = "kannada"
#     salary = 1000000

#     def getinfo(self):#u can make self as anything like slf , make .....
#           inside method
#         print(f"{self.name} persued {self.language} and obtained salary of {self.salary}")

# trainer2 = Employee()
# trainer2.name = "Ganesha"#instance attributes
# trainer2.salary = 10000
# trainer2.getinfo()

# STATIC METHOD
# Sometimes we need a function that does not use the self-parameter. 

# class Employee:
#     name = "harish"#attributes
#     language = "kannada"
#     salary = 1000000

#     @staticmethod
#     def greet():
#         print(f"Good morning  ")

# trainer2 = Employee()
# trainer2.name = "Ganesha"#instance attributes
# trainer2.salary = 10000
# trainer2.greet()

# Constructor(__INIT__() CONSTRUCTOR)


# class car:
#     def __init__(self , model , year):
#          self.model =model 
#          self.year =  year 

#     def getinfo(self):
#         print(f"Your car {self.model} has waranty period till {self.year + 6}  ")

# ciaz =car("ciaz" , 2026)
# ciaz.getinfo()


# practice set 

# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

# class Programmer:
#     work = "Microsoft"

#     def __init__(self , name , age , salary):
#         self.name = name
#         self.age = age
#         self.salary =salary
# emp1 = Programmer("Ajay",29,4500000)
# print(f"Name:{emp1.name}\nAge:{emp1.age}\nWork:{emp1.work}\nSalary:{emp1.salary}")


# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

# class Calculator:

#     def __init__(self , n):
#         self.n = n

#     def cal_sq(self):
#         print(f"The square of {self.n} is {self.n*self.n}")
    
#     def cal_cube(self):
#         print(f"The cube of {self.n} is {self.n*self.n*self.n}")

#     def cal_sqrt(self):
#         print(f"The square root  of {self.n} is {self.n**1/2}")

# num = Calculator(16)
# num.cal_sq()
# num.cal_cube()
# num.cal_sqrt()

# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

# class demo:
#     a = 34

# b = demo()
# print(f"Before setting object attribute value of a:{b.a}")
# b.a = 2
# print(f"After setting object attribute value of a:{b.a}")
# print("Class attribute does not change")

# 4. Add a static method in problem 2, to greet the user with hello.

# class Calculator:

#     def __init__(self , n):
#         self.n = n

#     @staticmethod
#     def greet():
#         print("Hello")

#     def cal_sq(self):
#         print(f"The square of {self.n} is {self.n*self.n}")
    
#     def cal_cube(self):
#         print(f"The cube of {self.n} is {self.n*self.n*self.n}")

#     def cal_sqrt(self):
#         print(f"The square root  of {self.n} is {self.n**1/2}")

# num = Calculator(16)
# num.greet()
# num.cal_sq()
# num.cal_cube()
# num.cal_sqrt()

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways

# from random import randint
# class Train:
#     seats = 10
#     fare = randint(100,2000)
#     def __init__(self, train_no , seat_req):
#         self.train_no = train_no
#         self.seat_req = seat_req
#         self.avail_seats = Train.seats
#         self.fair = Train.fare

#     def book(self):
#         print(f"Seats successfully book in Train no :{self.train_no}\n Total available seats : {self.avail_seats - self.seat_req}")

#     def status(self):
#         print(f"Train will be arriving shortly . Total available seats : {self.avail_seats - self.seat_req}")

#     def fare(self):
#         print(f"The fare of this ride is {randint(100,2000)}")

# tr = Train(23004869,4)
# tr.book()
# tr.status()
# tr.fare()

# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

# yes we can change the self-parameter inside a class to something else

# class Calculator:

#     def __init__(harry , n):
#         harry.n = n

#     def cal_sq(harry):
#         print(f"The square of {harry.n} is {harry.n*harry.n}")
    
#     def cal_cube(harry):
#         print(f"The cube of {harry.n} is {harry.n*harry.n*harry.n}")

#     def cal_sqrt(harry):
#         print(f"The square root  of {harry.n} is {harry.n**1/2}")

# num = Calculator(16)
# num.cal_sq()
# num.cal_cube()
# num.cal_sqrt()