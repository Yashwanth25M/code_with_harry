# List and tuples

# list(mutable)
# friends = ["Apple" , "Akash" , "orange" , False , 3.14 , 2]

# list indexing works same as strings

# friends[1] = "Ajay" #updating items

# List methods

# l = [1 , 8 , 7 , 2 , 21 ,15]

# l.append(11)#insert 11 to end if list
# print(l)
# l.insert(2,99)#insert item to particular index
# print(l)
# l.sort()#sorts in ascending order
# print(l)
# l.reverse()#reverses the list
# print(l)
# l.pop()#removes  last item
# print(l)
# # l.pop(2)#removes  item at index 2
# # # print(l)
# # l.remove(99)#removes item  99 from list
# # print(l)


# Tuples(immutable)
# same as list but immutabel
# a = (1 , 2 , 3 , 4)

# b=()#empty tuple
# print(type(b))

# b=(1,)#single element  tuple
# print(type(b))

# a.count(1)#returns number of occurences
# a.index(3)#returns index of particular item


# Practise set

# 1. Write a program to store seven fruits in a 
# list entered by the user.

# fruit = []
# f1 = input("Enter fruit 1:")
# fruit.append(f1)
# f2 = input("Enter fruit 2:")
# fruit.append(f2)
# f3 = input("Enter fruit 3:")
# fruit.append(f3)
# f4 = input("Enter fruit 4:")
# fruit.append(f4)
# f5 = input("Enter fruit 5:")
# fruit.append(f5)
# f6 = input("Enter fruit 6:")
# fruit.append(f6)
# f7 = input("Enter fruit 7:")
# fruit.append(f7)
# print(fruit)

# fruit = []
# for i in range(0,8):
#     f=input(f"Enter fruit {i+1}:")
#     fruit.append(f)
# print(fruit)

# 2. Write a program to accept marks of 6 students and display 
# them in a sorted manner.

# marks = []
# for i in range(0,8):
#     f=int(input(f"Enter marks {i+1}:"))
#     marks.append(f)
# marks.sort()
# print(marks)

# 3. Check that a tuple type cannot be changed in python.

# a = (34 , "array" , 34)
# a[2] = 64#Throws an error as tuples are immutable

# 4. Write a program to sum a list with 4 numbers.

# l = [ 1 , 2, 3  , 3]
# print(sum(l))


# 5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)

# a = (7, 0, 8, 0, 0, 9)
# print(a.count(0))