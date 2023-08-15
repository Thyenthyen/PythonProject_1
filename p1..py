# Program Name: p1.py
# My Name: Thuyen Nguyen
# Python version: 3.10.4
# Date: 04/09/2022 - 4/10/2022
# Description:
'''
Save and submit it as p1.py
1)Type up the Example program output.py program (don't copy/paste), including the comments, and get it working.
2)When the program runs, copy/paste how the program ran at the bottom of your program as a multi-line comment '''     ''', then save the file
3)Submit output.py
'''

print('hello world') # single quote
print("hello world") # double quote
print("he\nllo") # \n insert a new line (same as presing Enter)

#VARIABLES are named storage locations for numbers, strings, lists
#STRING is anything enclosed in quotes "Hello Word", that's a string
#NUMBER can be either a FLOAT (Ex: 9.3) or an INTEGER (Ex: 9.0)
#LISTS are things like [1,2,3] or ["Alex", "Stoykov"]
myName = "ALex" # declare/intialize string variable myName
Weight = 183.5483 # declare/initialize float variable Weight
Age = 33 # declare/initialize int variable Age
Grades = [90,77,88]
nameZ = ["ALex", "Stoykov"]

print ("Hello, Alex")
print ("Your weight is ", Weight, "and your age is ", Age)
print ("Your weight is %.2f and your age is %i" %(Weight, Age))
print ("Lists: grades =",Grades,"nameZ=",nameZ)
print ("This is how you print", end=' ')
print ("on the same line")

'''
============ RESTART: C:/Users/Thyen/OneDrive/Máy tính/week 1 p1.py ============
hello world
hello world
he
llo
Hello, Alex
Your weight is  183.5483 and your age is  33
Your weight is 183.55 and your age is 33
Lists: grades = [90, 77, 88] nameZ= ['ALex', 'Stoykov']
This is how you print on the same line
'''
