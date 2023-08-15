# Program name: p41
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/8/2022
# Description:
'''
Write a function which outputs as many crosses
as the parameter 'numCrosses' indicates.

def stars(numCrosses):
For example, when parameter 'numCrosses' equals 5,
the function displays the following:

+ 
+ + 
+ + + 
+ + + + 
+ + + + +
You are not allowed to use string "concatenation" or multiplication.
Also the use of a list and appending to a list is not permitted.
You must solve the problem using 2 loops (one 'for' loop nested in the other).
'''

def stars(numCrosses):
    for row in range(0,numCrosses,1):
        print('+', end= ' ')
        for i in range(0,row,1):
            print('+',end= ' ')
        print() # show a new line after the extra star


stars(5)
stars(7)

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p41.py ==========
+ 
+ + 
+ + + 
+ + + + 
+ + + + + 
+ 
+ + 
+ + + 
+ + + + 
+ + + + + 
+ + + + + + 
+ + + + + + + 
'''
