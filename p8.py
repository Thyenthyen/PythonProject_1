# Program name: p8
# Your Name: Ngoc Dan Thuyen Nguyen
# 5/3/2022
# Python 3.10.4
# Description:
'''
Write a program to print a multiplication table for float
values 0.1, 0.2 and 0.3.
The Output should use the placeholder (%) to control column widths.
'''

print('     0.1   0.2   0.3')
print('0.1  %.2f  %.2f  %.2f' %(.1*.1, .2*.1, .3*.1))
print('0.2  %.2f  %.2f  %.2f' %(.1*.2, .2*.2, .3*.2))
print('0.3  %.2f  %.2f  %.2f' %(.1*.3, .2*.3, .3*.3))

'''
===== RESTART: C:/Users/Thyen/AppData/Local/Programs/Python/Python310/p8.py ====
     0.1   0.2   0.3
0.1  0.01  0.02  0.03
0.2  0.02  0.04  0.06
0.3  0.03  0.06  0.09
'''
