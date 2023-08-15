# Program name: p9
# Your Name: Ngoc Dan Thuyen Nguyen
# 5/3/2022
# Python 3.10.4
# Description:
'''
Write a program to compute a person's height and print out a message.
The user will input their height in feet and inches.
The program will convert the feet and inches into total_inches,
and then print a message.
If the total inches is greater than 72, the message should be
something like, "You're tall."
If the total inches is between 5' and 6', a different message should
appear, like "You are average"
If the total inches is less than 60, another message should
appear, like "You are vertically challenged"
'''

#Ask the user for height (feet and inches)
print('Enter your height')
feet = float(input('feet:'))
inches = float(input('inches:'))

#Calculate the totalInches
totalInches = feet*12 + inches

#Show result
#print('%.0f feet %.0f inch(es) = %.0 inches' %(feet, inches, totalInches))
print( feet, 'feet', inches, 'inch(es) =', totalInches, 'inches')

#Print the message
if totalInches > 72:
    print("You're tall.")
elif totalInches > 60 and totalInches < 70:
    print("You're average.")
elif totalInches < 60:
    print("You are vertically challenged.")

'''
===== RESTART: C:/Users/Thyen/AppData/Local/Programs/Python/Python310/p9.py ====
Enter your height
feet:5
inches:1
5.0 feet 1.0 inch(es) = 61.0 inches
You're average.
'''
