# Program name: p20
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/3/2022
# Description:
'''
Write a program that reads in X whole numbers and outputs (1) the sum of all
positive numbers, (2) the sum of all negative numbers, and (3) the sum of all
positive and negative numbers. The user can enter the X numbers in any different
order every time, and can repeat the program if desired.
'''


X = int(input('How many numbers would you like to enter?'))

sumAll = 0
sumNeg = 0
sumPos = 0
for index in range(0,X,1):
    number = float(input('Please enter number %i:' %(index+1)))
    
    sumAll = sumAll + number

    if number<0:
        sumNeg += number

    if number>0:
        sumPos += number

        
print('The sum of positive numbers =',sumPos)    
print('The sum of negative numbers =',sumNeg)
print('The sum of all numbers =', sumAll)

while (True):
    try:
        out= str(input('Would you like to repeat? (y)(n):'))
        if out=='n':
            break
    except ValueError:
        print('You did not enter invalid answer. Please enter again')
        continue

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p20.py ==========
How many numbers would you like to enter?4
Please enter number 1:3
Please enter number 2:-4
Please enter number 3:-6
Please enter number 4:5
The sum of positive numbers = 8.0
The sum of negative numbers = -10.0
The sum of all numbers = -2.0
Would you like to repeat? (y)(n):n
'''

        
        
        

