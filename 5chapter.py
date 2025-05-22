# Dictionary and sets

# Dictionary(mutable):Collection of key-value pairs

# marks = {"a" : 2 , "b" :3 , 'c' : 8}
# print(marks)
# print(marks["a"])#accesing items
# marks["a"]=7 #updating dictionary
# print(marks)

# Dictionary methods
# a1 =  {"a" : 2 , "b" :3 , 'c' : 8}
# print(a1.items())
# print(a1.keys())
# print(a1.values())
# a1.update({"b" : 8 , "d" : 7})#updating dictionary and adding new items 
# print(a1)
# a1["a"]=7 #updating dictionary
# print(a1)
# print(a1.get("a"))#returns value , if key not present does not raises an error
# print(a1.get("f"))
# print(a1["f"])#this raises an error as "f" is not present

# more methods available in docs.python.org

# Set
# s = set()#This is empty set
# set is same  as list but without indexing ,without repetation

# sets methods
# s = {23 , 3 , 45 , 78 ,25}
# s.add(30)#adds to existing set
# print(s)

# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.


# Operations
# s = {23 , 3 , 45 , 78 ,25}
# print(len(s))
# s.remove(23)
# print(s)
# s.pop()
# print(s)
# s.clear()#clears whole set
# print(s)

# Union and itersection

# Practise set

# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

# words = {"sahaya" : "help" , "oota" : "food"}
# word=input("Enter the word to know meaning :")
# print(words.get(word) )

# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).

# s = set()
# for i in range(0,8):
#     n = int(input(f"Enter number {i+1}:"))
#     s.add(n)
# print(s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

# s = set()
# s.add(18)
# s.add("18")
# print(s)
# Yes we have a set with 18 (int) and '18' (str) as a value in it

# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))

# 5. s = {}
# What is the type of 's'?

# s = {}
# print(type(s))#dictionary ,empty set look like this[s=set()]

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# d = {}
# for i in range(0,4):
#     k =input("Enter your name:")
#     v =input("Enter your favorite language:")
#     d[k]=v
#     print(f"Total number of inputs:{i+1}")
# print(d)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

# if two names are same then language of last entered will be updated to earlier one

# 8. If languages of two friends are same; what will happen to the program in problem 6?

# Then return normal dictionary with  languages of two friends are same

# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

# sets are not indexed so cannot change the values inside a list
# we cannot include list inside set