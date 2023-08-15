# Program name: p33
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/7/2022
# Description:
'''
If you are given three sticks, you may or may not be able to arrange them in a
triangle. For example, if one of the sticks is 12 inches long and the other two
are one inch long, you will not be able to get the short sticks to meet in the
middle.

For any three sticks, there is a simple test to see if it is possible to form a
triangle:
“If any of the three sticks is greater than the sum of the other two, then you
cannot form a triangle. Otherwise, you can.”

Write a function named isTriangle(a,b,c) that has three sides a,b,c  as
parameters.

The function returns either True or False, depending on whether you can form a
triangle from the sides with the given lengths.
'''


def isTriangle(a,b,c):
    if a > b+c:
        return False
    elif b > a+c:
        return False
    elif c > a+b:
        return False
    return True

#function call,test the function above
print("Three sticks with length 3,4,5 can form a triangle:",isTriangle(3,4,5))
print("Three sticks with length 3,5,4 can form a triangle:",isTriangle(3,5,4))
print("Three sticks with length 4,3,5 can form a triangle:",isTriangle(4,3,5))
print("Three sticks with length 4,5,3 can form a triangle:",isTriangle(4,5,3))
print("Three sticks with length 5,4,3 can form a triangle:",isTriangle(5,4,3))
print("Three sticks with length 5,3,4 can form a triangle:",isTriangle(5,3,4))
print("Three sticks with length 20,3,4 can form a triangle:",isTriangle(20,3,4))
print("Three sticks with length 3,20,4 can form a triangle:",isTriangle(20,3,4))
print("Three sticks with length 3,4,20 can form a triangle:",isTriangle(3,4,20))


'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p33.py ==========
Three sticks with length 3,4,5 can form a triangle: True
Three sticks with length 3,5,4 can form a triangle: True
Three sticks with length 4,3,5 can form a triangle: True
Three sticks with length 4,5,3 can form a triangle: True
Three sticks with length 5,4,3 can form a triangle: True
Three sticks with length 5,3,4 can form a triangle: True
Three sticks with length 20,3,4 can form a triangle: False
Three sticks with length 3,20,4 can form a triangle: False
Three sticks with length 3,4,20 can form a triangle: False
'''













