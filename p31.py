# Program name: p31
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/7/2022
# Description:
'''
Write a function that has an integer N as
parameter and returns true if N is even.

Hint: A number N is even if N % 2  == 0

Be sure to type the function name and the
function calls below, copy/pasting it will give you errors!
'''

def isEven(N):
    if N%2 == 0:
        return True
    return False

#function call
print('Test Run1:')
print('3 is even:', isEven(3))
print('\nTest Run2:')
print('4 is even:', isEven(4))


'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p31.py ==========
Test Run1:
3 is even: False

Test Run2:
4 is even: True
'''
