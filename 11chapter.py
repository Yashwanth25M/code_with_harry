# Inheritance

# traditional way
# class Employee:
#     def display(self):
#         print("This is display")

# class Student:
#     def display(self):
#         print("This is display")
#     def getinfo(self):
        # print("This will get info")

# The same task can be carried outlike this
# class Employee:
#     def display(self):
#         print("This is display")

# class Student(Employee):#inheritence 
#     def showLanguage(self):
#     def getinfo(self):
#         print("This will get info")   

# Multiple inheritence

# class Employee:
#     company = "ITC"
#     name = "Default name"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the company is {self.company}")

# class Coder:
#     language = "Python"
#     def printLanguages(self):
#         print(f"Out of all the languages here is your language: {self.language}")
     


# class Programmer(Employee, Coder):
#     company = "ITC Infotech"
#         print(f"The name is {self.company} and he is good with {self.language} language")


# a = Employee()
# b = Programmer()

# b.show()
# b.printLanguages()
# b.showLanguage()


# Multi-level inheritence 

# class Employee:
#     a = 2

# class programmer(Employee):
#     b = 2

# class manager(programmer):
#     c = 3

# o = Employee()
# print(o.a)
# b = programmer()
# print(b.a)
# print(b.b)
# c = manager()
# print(c.a)
# print(c.b)
# print(c.c)

# /super method

# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")
#     a = 1 

# class Programmer(Employee):
#     def __init__(self):
#         print("Constructor of Programmer")
#     b = 2 

# class Manager(Programmer):
#     def __init__(self):


#         super().__init__()#calls super class also(in this case calls programmer class also)
#         print("Constructor of Manager")
#     c = 3

# o = Manager()
# print(o.a, o.b, o.c)

# Class method

# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

#classmethod ignores the instance attribute and carry out with class attribute

# class card: 
#     a = 2
#     @classmethod
#     def show(cls):
#         print(f"The attribute value of a is {cls.a}")
# c = card()
# c.a = 22
# c.show()


# @PROPERTY DECORATORS
# 

# class Employee:
#     a = 1
    
#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")

#     @property #in simple we can make it return anything
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name (self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = Employee()
# e.a = 45

# e.name = "Harry Khan"
# print(e.fname, e.lname)

# e.show()


# Operator overloading


# class Number:
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n

# n = Number(1)
# m = Number(2)

# print(n + m)



# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)


# Practice set(copy pasted)


# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

# class TwoDVector:
#         def __init__(self , i , j):
#                 self.i = i
#                 self.j = j
#         def display(self):
#                 print(f"The 2D vectors are {self.i}i+{self.j}j ") 

# class ThreeDVector(TwoDVector):
#         def __init__(self, i , j , k):
#                 super().__init__( i ,j )
#                 self.k = k
#         def display(self):
#                 print(f"The 3D vector are {self.i}i+{self.j}j+{self.k}k")               

# m = TwoDVector(1 , 2)
# n = ThreeDVector(1 , 3 , 3)
# m.display()
# n.display()


# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

# class Animal:
#     pass

# class Pets(Animal):
#     pass

# class Dog(Pets):
#     def bark(self):
#         print("BOW BOW!!")

# a = Dog()
# a.bark()

# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

# class Employee:
#     salary = 234
#     increment = 20 
    
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))

#     @salaryAfterIncrement.setter 
#     def salaryAfterIncrement(self, salary):
#         self.increment =  ((salary/self.salary) -1)*100 

# e = Employee()
# e.salaryAfterIncrement = 280.8
# print(e.increment)


# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         real_part = self.r * c2.r - self.i * c2.i
#         imag_part = self.r * c2.i + self.i * c2.r
#         return Complex(real_part, imag_part)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
        
# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2)
# print(c1*c2)

