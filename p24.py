# Program name: p24
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/4/2022
# Description:
'''
Write a program that generates X random integers Num.
Num is a random number between 20 to 50. 
X is a random number between 10 to 15.
Calculate and show the Smallest, Largest, Sum,
and Average of those numbers.
You are not allowed to use Python functions sample(),
min(), max(), average(), sort(), sorted()!!
'''

from random import randint

X = randint(10,15)
sumAll = 0
print('X =',X)

for i in range(0,X,1):
    number = randint(20,50)
    sumAll += number # adding every number to the sum
    print(number, end=' ')# end='' prevent creating a new line
                                #^ can type sth in this space
    
    #first random number is when i=0
    if i == 0:
        smallest = number
    else:# for all any number after the first
        if number < smallest:
            smallest = number

    if i == 0:
        largest = number
    else:# if any number after the first
        if number > largest:
            largest = number

print('\nSmallest =',smallest)
print('Larget =', largest)
print('Sum =',sumAll)
print('Average = %i/%i = %.1f' %(sumAll,X,(sumAll/X)))

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p24.py ==========
X = 13
31 28 31 33 46 32 49 37 36 39 26 30 35 
Smallest = 26
Larget = 49
Sum = 453
Average = 453/13 = 34.8

'''


        
