# String
# strings are immutable

# a = "abcd" # content inside " " are string
# a = 'abcd' # content inside ' ' are string
# a = ''''abcd''' # Multiline string
# a = """abcd""" # Multiline string

# String slicing

# indexing of strings 
#  a  b  c  d  e  f  g  h
#  0  1  2  3  4  5  6  7 
# -8 -7 -6 -5 -4 -3 -2 -1

# to find lengtht
# a = "abcdegh"
# print(len(a))

# [start : end : step]

# a = "abcdegh"
# b = a[1]
# print(b)#print single at particular index
# c = a[0:5]
# print(c) #prints abcde excluding 5th index
# d = a[:5]
# print(d) #same as a[0:5]
# e = a[0 : 7]
# print(e)#prints whole string
# f = a[0:]
# print(f)#same as a[0 : 7]
# g = a[ -8 : -1]#better convert to corresponding positive indices
# print(g)

# for easy calculate length using len function
# for string a length is 7 , add 1
# now take negative indices and perform below operation
#  8(len+1)-8(indices provided) = 0
#  8(len+1)-1(indices provided) = 7
#  now its a[0:7] which is "abcdeg"

# string slicing with skip values
# a="amaze"
# b = a[0 : 5 : 2]#if skip value is 2 then decrease it by 1 
# # print(b)

# # String function 
# str = "abcdefgh"
# print(len(str))#returns length
# print(str.endswith("gh"))#returns true if it ends with
# print(str.startswith("ab"))#returns true if it starts with
# print(str.count("a"))#returns number of occurences
# print(str.capitalize())#capitalize first alphabet
# print(str.title())#capitalize first alphabet of each word
# print(str.upper())#capitalize whole string
# print(str.lower())#lowers
# print(str.find("c"))#returns index
# print(str.replace("h" , "i"))#replaces all occurences

# escape sequences
# print("Hello \n world") #prints world in next line
# print("Hello \t world") #prints world with tab space
# print("to print single quotes \'text under single quote\'")
# print('to print single quotes \"text under double quote\"')


# Practice set 

# 1. Write a python program to display a user entered name followed 
# by Good Afternoon using input () function

# name = input("enter your name : ")
# print(f"{name} Good Afternoon")

# 2. Write a program to fill in a letter template
#  given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# name = input("Enter name:")
# date = input("Enter date :")
# print(letter.replace("<|Name|>" , name).replace("<|Date|>" , date))

# 3. Write a program to detect double space in a string

# string =" Hello  world"
# print("  " in string) #using membership operator

# 4. Replace the double space from problem 3 with single spaces

# string ="Hello  world"
# print(string.replace("  " , " "))

# 5. Write a program to format the following letter using escape
# sequence characters.
# letter = "Dear Harry,\n \t This python course is nice.\n\t\t Thanks!"
# print(letter)