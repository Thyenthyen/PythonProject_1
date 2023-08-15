# Program name: p15
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/3/2022
# Description:
'''
Write a program that asks the user to enter 4 numbers (positive or negative).
The program shows:
the sum of all numbers (sumAll)
the sum of positive numbers (sumPos)
the sum of negative numbers (sumNeg)
'''

a = float(input('Enter number 1:'))
b = float(input('Enter number 2:'))
c = float(input('Enter number 3:'))
d = float(input('Enter number 4:'))

sumAll=0
sumAll=a+b+c+d
print('Sum of all is', sumAll)

sumPos=0
if a > 0:
    sumPos += a
if b > 0:
    sumPos += b
if c > 0:
    sumPos += c
if d > 0:
    sumPos += d
print('Sum of positive numbers is', sumPos)

sumNeg=0
if a < 0:
    sumNeg += a
if b < 0:
    sumNeg += b
if c < 0:
    sumNeg += c
if d < 0:
    sumNeg += d
print('Sum of negative numbers is', sumNeg)

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p15.py ==========
Enter number 1:1
Enter number 2:-1
Enter number 3:2
Enter number 4:3
Sum of all is 5.0
Sum of positive numbers is 6.0
Sum of negative numbers is -1.0
'''



