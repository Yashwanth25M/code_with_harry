#  FILE I/O

# Basic program to open a file and read the content
# w = open("read.txt")
# data = w.read()
# print(data)
# w.close()

# Basic program to open a file and write the content
# s = "Veggie is good"
# w = open("read.txt" , "w")
# w.write(s)
# print("Done writing !!")
# w.close()

# file function
# w = open("read.txt")
# data = w.readlines()#provides content inside a list(provide whole content inside a list)
# print(data,type(data))
# w.close()

# Accessing each line
# w = open("read.txt")
# line1 = w.readline()
# print(line1,type(line1))
# line2 = w.readline()
# print(line2,type(line2))
# line3 = w.readline()
# print(line3,type(line3))#prints a respective line
# line4 = w.readline()
# print(line4,type(line4))

# f = open("read.txt")
# line = f.readline()
# while ( line != ""):
#     print(line)
#     line = f.readline()
# f.close()

# MODES OF OPENING A FILE
# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode.

# s = "Dont be vegan \n "
# f = open("read.txt","a")#append text(s) to file
# f.write(s)
# f.close()

# with open("read.txt") as w:
#     print(w.read())
#removes the burden of closing a file

# Practice set

# # 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’

# q = open("poem.txt")
# line  = q.readline()
# while(line != ""):
#     if("twinkle" in line):
#         print('The word " twinkle" is present')
#         break
#     else:
#         print('The word " twinkle" is not present')
#     line  = q.readline()
# q.close()

# q = open("poem.txt")
# line  = q.read()
# if("twinkle" in line):
#     print('The word " twinkle" is present')
# else:
#     print('The word " twinkle" is not present')

# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore 
# whenever the game() function breaks the Hi-score.

# import random
# def game():
#     print("You are playing the game")
#     score = random.randint(1,100)
#     with open("Hi-score.txt") as w:
#         hiscore = w.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"your score:{score}")
#     if(score > hiscore):
#         with open("Hi-score.txt","w") as f:
#             f.write(str(score))
#     return score
# game()

# def game(n):
#     print("You are playing a game")
#     with open("Hi-score.txt") as w:
#         x = w.read()
#         print(f"Your last score {x}")
#         if (x != ""):
#             x = int(x)
#         else:
#             x = 0
#         print(f"Your score is {n}")
#         if( n > x):
#             with open("Hi-score.txt" , "w") as f:
#                 f.write(str(n))
# game(101)


# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

# def table(n):
#     table = ""
#     for i in range (1,11):
#         table += f"{n} X {i} = {n*i} \n"

#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)

# for i in range(2,21):
#     table(i)


# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.

# word = "Donkey"

# with open ("don.txt" , "r") as d:
#     content = d.read()

# content_new = content.replace(word,"######")

# with open("don.txt","w") as w:
#     w.write(content_new)

# 5. Repeat program 4 for a list of such words to be censored.

# words = ["donkey" , "shit" ]
# with open ("don.txt" , "r") as d:
#     content = d.read()

# for word in words:
#     content = content.replace(word,"#"*len(words))

# with open("don.txt","w") as w:
#     w.write(content)

# 6. Write a program to mine a log file and find out whether it contains ‘python’.

# word = "python"
# with open("log_file.txt") as w:
#     content = w.read()
#     if(word in content):
#         print('The word "python" is present in log file')
#     else:
#         print('The word "python" is not present in log file')

# 7. Write a program to find out the line number where python is 
# present from ques 6.

# with open("log_file.txt") as w:
#     lines = w.readlines() 
# i=1

# for line in lines:
#     if("python" in line):
#             print(f'The word "python" is present in {i}th line of log file')
#     i += 1


# 8. Write a program to make a copy of a text file “this. txt”

# with open("this.txt") as w:
#     content = w.read()
# with open("this_copy.txt","w") as w:
#     w.write(content)

# 9. Write a program to find out whether a file is identical 
# & matches the content of another file.

# with open("this.txt") as a:
#     con1 = a.readlines()
# with open("this_copy.txt") as a:
#     con2 = a.readlines()

# if (con1 == con2):
#     print("files are identical  & matches the content of another file.")
# else:
#     print("files are  not identical  &  does not matches the content of another file.")



#   10. Write a program to wipe out the content of a file using python.
  
# with open("don.txt","w") as w:
#     w.write("")


# 11. Write a python program to rename a file to “renamed_by_ python.txt

# with open("con1.txt") as f:
#     con = f.read()
# with open("renamed_by_ python.txt","w") as d:
#     d.write(con)