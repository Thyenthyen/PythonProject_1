# Program name: p28
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/7/2022
# Description:
'''
Write a function which given two integer parameters
Returns their sum...unless the two values are the same,
then the function Returns their doubled sum.
Be sure to type the function name and the function
calls below, copy/pasting it will give you errors!
'''



def sum_double(a,b):
    if (a != b):
        return a + b

    return (a + b) * 2


print(sum_double(1,2))
print(sum_double(2,2))

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p28.py ==========
3
8
'''
