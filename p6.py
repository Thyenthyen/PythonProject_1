# Program name: p6
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 5/3/2022
# Description:
'''
Write a program to compute a person's height.
INPUT: User will enter two whole numbers: feet and inches.
OUTPUT: Values input & total in inches.
INPUT VALIDATION: Make sure that feet and inches are positive values.
'''

#ask for height ( feet and inches)
print('Enter your height')
feet   = int(input('feet:'))
inches = int(input('inches:'))

#calculate the total inches
totalInches = feet * 12 + inches

#show result
print( feet, 'feet', inches, 'inch(es) =', totalInches, 'inches')

'''
===== RESTART: C:/Users/Thyen/AppData/Local/Programs/Python/Python310/p6.py ====
Enter your height
feet:5
inches:1
5 feet 1 inch(es) = 61 inches
'''
