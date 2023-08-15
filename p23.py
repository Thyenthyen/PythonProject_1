# Program name: p23
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/4/2022
# Description:
'''
Write a program to let a child practice arithmetic skills.
The program should first ask for what kind of practice is wanted: addition(1),
subtraction(2), or multiplicatio(3)... (no division).
Then, the program will have a loop for each of the the desired operations that
lets the user repeat the practice as many times as desired,
Two random numbers will be generated (0 - 9), and the child will have to add,
subtract or multiply them.
If the child answers the question correctly, congratulate them, and give them
two different numbers to try.
If the child answers incorrectly, the problem should be repeated (with the two
same numbers).
Note: You are not allowed to use the eval() or sum() functions!
'''


from random import randint
while(True):
    num1 = randint(0,9)
    num2 = randint(0,9)
    op = int(input('Would you like to add(1), subtract (2) or multiply(3):'))
    if op == 1: #add
        answer = int(input('What is %i + %i =' %(num1,num2)))
        while answer != num1+num2:
            answer = int(input('That is incorrect, what is %i + %i =' %(num1,num2)))
        repeat = input('Correct! Would you like to try again? (y/n):')
        if repeat != 'y':
            print('Thank you for playing!')
            break
    elif op == 2: #subtract
        answer = int(input('What is %i - %i =' %(num1,num2)))
        while answer != num1-num2:
            answer = int(input('That is incorrect, what is %i - %i =' %(num1,num2)))
        repeat = input('Correct! Would you like to try again? (y/n):')
        if repeat != 'y':
            print('Thank you for playing!')
            break
    elif op == 3: # multiply
        answer = int(input('What is %i * %i =' %(num1,num2)))
        while answer != num1*num2:
            answer = int(input('That is incorrect, what is %i * %i =' %(num1,num2)))
        repeat = input('Correct! Would you like to try again? (y/n):')
        if repeat != 'y':
            print('Thank you for playing!')
            break
    else:
        print('Please try again')

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p23.py ==========
Would you like to add(1), subtract (2) or multiply(3):12
Please try again
Would you like to add(1), subtract (2) or multiply(3):1
What is 6 + 9 =19
That is incorrect, what is 6 + 9 =15
Correct! Would you like to try again? (y/n):y
Would you like to add(1), subtract (2) or multiply(3):3
What is 5 * 3 =26
That is incorrect, what is 5 * 3 =15
Correct! Would you like to try again? (y/n):n
Thank you for playing!
'''

