# Program name: p29
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/7/2022
# Description:
'''
 The absolute value of 1 is 1, and the absolute
value of -1 is also 1.
 Write a function that calculates the absolute value
and returns the absolute value of a number.
 Do not just use the built-in python function abs()!
You must write the definition yourself!
 Be sure to type the function name and the function calls
below, copy/pasting it will give you errors!
'''


def absolute():
    a = float(input('Enter a positive value or negative value:'))
    if a >= 0:
        print('The absolute value of',a,'is', a)
    if a < 0:
        a_after = a*(-1)
        print('The absolute value of',a,'is',a_after )
    
    return a

absolute()
absolute()

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p29.py ==========
Enter a positive value or negative value:1
The absolute value of 1.0 is 1.0
Enter a positive value or negative value:-1
The absolute value of -1.0 is 1.0
'''

