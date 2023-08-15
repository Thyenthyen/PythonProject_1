# Program name: p12
# Your Name:  Thuyen Nguyen
# Python Version: 3.10.4
# 5/3/2022
# Description:

'''
Write a program to determine if the user can vote.
The program will ask the user a series of questions - age,
citizenship and registration. The user will receive a message
as to whether or not s/he may vote -- yes, no (with a reason - too young,
not a citizen, hasn't registered to vote).

Be sure to test your program at least 4 times:
The user can vote
The user can't vote because they are not old enough.
The user can't vote because they are not old enough and not a citizen.
The user can't vote because they are not old enough, not a citizen, not registered.
Note: You must be over 18, registered , and a citizen to vote.

'''

# ask user for input
age = int(input('Please enter age:'))
citizen = input('Are you citizen? (yes or no):')
registered = input('Are you registered? (yes or no):')

# check if they can vote
if age >= 18 and citizen == 'yes' and registered == 'yes':
    print('congratulations, you can vote!')
else:
    print('You cannot vote.')
    if age < 18:
        print('You are not old enough.')
    if citizen != 'yes':
        print('You are not a citizen.')
    if registered != 'yes':
        print('You are not registered.')


'''
==== RESTART: C:/Users/Thyen/AppData/Local/Programs/Python/Python310/p12.py ====
Please enter age:16
Are you citizen? (yes or no):yes 
Are you registered? (yes or no):yes
You cannot vote.
You are not old enough.
You are not a citizen.

==== RESTART: C:/Users/Thyen/AppData/Local/Programs/Python/Python310/p12.py ====
Please enter age:16
Are you citizen? (yes or no):no
Are you registered? (yes or no):yes
You cannot vote.
You are not old enough.
You are not a citizen.

==== RESTART: C:/Users/Thyen/AppData/Local/Programs/Python/Python310/p12.py ====
Please enter age:16
Are you citizen? (yes or no):no
Are you registered? (yes or no):no
You cannot vote.
You are not old enough.
You are not a citizen.
You are not registered.

==== RESTART: C:/Users/Thyen/AppData/Local/Programs/Python/Python310/p12.py ====
Please enter age:20
Are you citizen? (yes or no):yes
Are you registered? (yes or no):yes
congratulations, you can vote!

'''
