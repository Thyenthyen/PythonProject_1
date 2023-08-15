# Program name: p6
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# 5/3/2022
# Description:

'''
Write a program which asks the user for a student's grade as a percent,
and then returns their letter grade.
Validate the input to make sure that the number is between 0 - 100.
If for any other number, say "ERROR" and ask for another number)

A is 90% or above
B is between 80% and 90%
C is between 70% and 80%
D is between 60% and 70%
F is under 60%

'''

# Ask for the grade as percent.
percent = float(input('Please enter your garde as percent:'))

# Validate input.
if percent < 0 or percent > 100:
    print('Error, the number must be between 0 to 100.')

# Display the grade.
    percent = float(input('Please enter your grade as percent:'))
if percent >=90 and percent <=100:
    print('You have an "A" ')
elif percent >=80 and percent <90:
    print('You have an "B" ')
elif percent >=70 and percent <80:
    print('You have an "C" ')
elif percent >=60 and percent <70:
    print('You have an "D" ')
elif percent >=0 and percent <60:
    print('You have an "F" ')

'''
==== RESTART: C:/Users/Thyen/AppData/Local/Programs/Python/Python310/p10.py ====
Please enter your garde as percent:-1
Error, the number must be between 0 to 100.
Please enter your grade as percent:66
You have an "D" 
'''
