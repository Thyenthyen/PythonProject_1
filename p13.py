# Program name: p13
 Thuyen Nguyen
# Python Version: 3.10.4
# 5/3/2022
# Description:

'''
Write a program to convert any given number of total cents(under 100) into
the correct number of: quarters, dimes, nickels, pennies.
'''

# Ask for the cents input
totalCents = int(input('Enter your total cents:'))

# Get the number of quaters
quarters = int(totalCents / 25)
if quarters > 0:
    print('You have', quarters, 'quarters')
    totalCents -= quarters * 25 #Get the remaining total cents.

# Get the number of dimes
dimes = int(totalCents / 10)
if dimes > 0:
    print('You have', dimes, 'dimes')
    totalCents = totalCents - dimes*10

# Get the number of nickels
nickels = int(totalCents / 5)
if nickels > 0:
    print('You have', nickels, 'nickels')
    totalCents = totalCents - nickels*5

# Get the number of pennies
pennies = int(totalCents / 1)
if pennies > 0:
    print('You have', pennies, 'pennies')

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p13.py ==========
Enter your total cents:66
You have 2 quarters
You have 1 dimes
You have 1 nickels
You have 1 pennies

========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p13.py ==========
Enter your total cents:16
You have 1 dimes
You have 1 nickels
You have 1 pennies

========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p13.py ==========
Enter your total cents:6
You have 1 nickels
You have 1 pennies

========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p13.py ==========
Enter your total cents:4
You have 4 pennies
'''
    
