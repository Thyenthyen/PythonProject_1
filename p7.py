# p7
# Your Name: Ngoc Dan Thuyen Nguyen
# 5/3/2022
# Python 3.10.4
# Description:
'''
Write a program to compute the circumference and area of a circle.
The user will input the radius of a circle.
Validate Input: Make sure that the radius is positive, or give an error message.
The program will show the circumference and area of a circle with that radius.
The answers should be rounded to the nearest tenth.
'''

#Define variable
PI = 3.1415

#Ask for the radius
radius = float(input('Enter radius:'))

#Validate Input
if radius < 0:
    print('Error, radius cannot be negative.')
else:
    area = PI*radius**2
    circumference = 2*PI*radius

#Show results
print('a circle with radius %.1f inches has' %radius)
print('area: %.1f square inches' %area)

'''
=========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p7.py ==========
Enter radius:12.66
a circle with radius 12.7 inches has
area: 503.5 square inches
'''
