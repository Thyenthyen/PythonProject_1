# Program Name: p5.py
# My Name: Ngoc Nguyen
# Python version: 3.10.4
# Date: 04/09/2022 - 4/10/2022
# Description:
'''
Write a program which computes the sum and product
of two numbers entered by the user.
Algorithm:
1)Ask the user to enter two numbers.
2)store those two numbers in 2 variables, num1, num2.
3)make two new variables sum = num1+ num2, and product = num1*num2
4)Then, output the sum and product of to the user.
'''

#enter values:
num1 = int( input("enter first number:"))
num2 = int( input("enter second number:"))

#calculate:
sum = num1+ num2
product = num1*num2

# results:
print(num1,"+",num2,"=",sum)
print(num1,"*",num2,"=",product)

''' test run:
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p5..py ==========
enter first number:3
enter second number:6
3 + 6 = 9
3 * 6 = 18
'''
