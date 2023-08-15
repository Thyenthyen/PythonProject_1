# Program name: p30
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/7/2022
# Description:
'''
Write a function which has two parameters, N and M.

The function returns True if N is evenly divisible
by M, and False otherwise.

Be sure to type the function name and the function
calls below, copy/pasting it will give you errors!
'''

def isDivisible(N,M):
    N = int(input('Enter integer N:'))
    M = int(input('Enter integer M:'))

    if N%M == 0:
        return True
    if N%M != 0:
        return False

#call the function
print('Test Run1:')
print('4 is evenly divisible by 2:',isDivisible(4,2))
print('\nTest Run2:')
print('5 is evenly divisible by 2:',isDivisible(5,2))

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p30.py ==========
Test Run1:
Enter integer N:4
Enter integer M:2
4 is evenly divisible by 2: True

Test Run2:
Enter integer N:5
Enter integer M:2
5 is evenly divisible by 2: False
'''
