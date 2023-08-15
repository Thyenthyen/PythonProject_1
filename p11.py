# Program name: p11
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 5/3/2022
# Description:

'''
Write a program to simulate rock-paper-scissors game.
Each players enters 'R', 'P', 'S' or 1, 2, 3 for Rock, Paper, Scissors.
The program then shows the winner on the basis of:
Paper covers Rock
Rock breack Scissors
Scissors cut Paper
Tie

'''

# Need this for randint()
import random


# Ask the use for input.
p1 = int(input('p1 enter 1 for rock, 2 for paper, 3 for scissors:'))
p2 = int(input('p2 enter 1 for rock, 2 for paper, 3 for scissors:'))
'''
Make random numbers for p1 and p2.
p1 = random.randint(1,3)
p2 = random.randint(1,3)
'''


# Show the generate values.
print('p1 =', p1)
print('p2 =', p2)

#Make the variables to store values for rock, paper, scissors.
rock = 1
paper = 2
scissors = 3

# Cases p1 wins.
if p1 == rock and p2 == scissors:
    print('p1 wins, rock breaks scissors.')
elif p1 == paper and p2 == rock:
    print('p1 wins, paper covers rock.')
elif p1 == scissors and p2 == paper:
    print('p1 wins, scissors cut paper.')

# Case p2 wins.
if p2 == rock and p1 == scissors:
    print('p1 wins, rock breaks scissors.')
elif p2 == paper and p1 == rock:
    print('p1 wins, paper covers rock.')
elif p2 == scissors and p1 == paper:
    print('p1 wins, scissors cut paper.')

# Case when p1, p2 tie.
if p2 == rock and p1 == rock:
    print('Tie')
if p2 == paper and p1 == paper:
    print('Tie')
if p2 == scissors and p1 == scissors:
    print('Tie')

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p11.py ==========
p1 enter 1 for rock, 2 for paper, 3 for scissors:2
p2 enter 1 for rock, 2 for paper, 3 for scissors:3
p1 = 2
p2 = 3
p1 wins, scissors cut paper.
'''







