# Program Name: p3.py
# My Name: Ngoc Nguyen
# Python version: 3.10.4
# Date: 04/09/2022 - 4/10/2022
# Description:
'''
1)Type up the Example input.py program below, including the comments, and get it working.
2)When the program runs, copy/paste the Output (in BLUE) at the bottom of your program as a multi-line comment '''     ''', then save the file.
3)Submit input.py
'''

name = input ("Please enter Your name: ") # this is a string
weightLbs = float(input ("Please enter Your weight in lbs: " )) # a float
age = int (input ("Please enter your age (whole number): " )) # an integer
weightKg= weightLbs*0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print ( weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end=' ') # end=' ' prevents new line
print ("kilograms ")

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p3..py ==========
Please enter Your name: Ngoc Nguyen
Please enter Your weight in lbs: 120
Please enter your age (whole number): 18
Hello Human Ngoc Nguyen your weight is
120.0 lbs
which equals = 54.43 kilograms 
'''
