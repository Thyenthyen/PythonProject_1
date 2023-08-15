# Program name: p26
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/4/2022
# Description:
'''
Write a program that generates a random list of numbers.
(start with an empty list and use append() )
The length of the list X can be a random number between 15 to 20.
Each of the random numbers on the list can be between 2 to 5.
Count how many times the number 3 appears.
You are not allowed to use python built-in function "count()"
or you'll get a Zero!

'''
#make an empty list
aList =[]

#add to the empty list
#aList.append(10)
#aList.append(20)
#print('aList =',aList)  

from random import randint
X = randint(15,20)
count = 0

for index in range(0,X,1):
    num = randint(2,5)
    aList.append(num)
    if num == 3:
        count += 1
print('Generating a list of %i numbers' %X)
print(aList)
print('The number 3 appears',count,'time(s)')


'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p26.py ==========
Generating a list of 15 numbers
[3, 4, 4, 3, 2, 4, 5, 4, 2, 2, 5, 4, 2, 2, 2]
The number 3 appears 2 time(s)
'''

