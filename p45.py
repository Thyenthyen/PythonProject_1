# Program name: p45
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/8/2022
# Description:
'''
Write a program that calculates and shows all prime numbers between 3 - 100.

Prime numbers can only be evenly (remainder 0) divided by itself and 1.

Example of PRIME NUMBER testing:
4 -> 4 : 2 = 2.0 , 4 is NOT a prime (because there is a Zero after the decimal)
5 -> 5 : 2 = 2.5 ; 5 : 3 = 1.67 ; 5 : 4 = 1.25,  5 is A PRIME (no Zero after
decimal)
6 -> 6 : 2 = 3.0 , 6 is NOT a prime (because there is a Zero after the decimal)
7 -> 7 : 2 = 3.5; 7 : 3 = 2.33; 7 : 4 = 1.75; 7 : 5 = 1.4; 7 : 6 = 1.17  7 is A
PRIME (no Zero after decimal)
'''

for numToTest in range(3,101,1):
    for i in range(2,numToTest,1):#start from 2 not 1 as below i-1
        if numToTest%i == 0:
            break # stop checking bc it's not a prime
        if numToTest%i != 0 and i == numToTest-1:
        # it's not devided by any number and go to the end of the list
            print(numToTest,'is a prime number')
 
'''
==================================================== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p45.py ===================================================
3 is a prime number
5 is a prime number
7 is a prime number
11 is a prime number
13 is a prime number
17 is a prime number
19 is a prime number
23 is a prime number
29 is a prime number
31 is a prime number
37 is a prime number
41 is a prime number
43 is a prime number
47 is a prime number
53 is a prime number
59 is a prime number
61 is a prime number
67 is a prime number
71 is a prime number
73 is a prime number
79 is a prime number
83 is a prime number
89 is a prime number
97 is a prime number
'''
