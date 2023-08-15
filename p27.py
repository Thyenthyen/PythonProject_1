# Program name: p27
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/4/2022
# Description:
'''
Write a program that generates a random list of letters.
# start with an
empty_list = [ ]
# and use
empty_list.append(Letter) # to add letters to the list
 The length of the list of letters changes every time you run the program.
 There can be a random number of X  letters on the list, where X is a
random number between 50 to 75.
 Each of the letters on the list is a random letter between
A to F (uppercase).
 Use a loop to generate the list and then Show the generated list of
letters to the user.
 Count and then show to the user how many times the letter B appears.
 In order to receive credit, you may not use python built-in function "count()" !
'''

empty_list = []

from random import randint
X = randint(50,75)
count = 0

for index in range(0,X,1):
    asciiNum = randint(65,70)
    empty_list.append(chr(asciiNum))
    if asciiNum == 66:
        count += 1

print('Made a list of', X,'letters')
print(empty_list)
print('The letter "B" appears',count,'time(s)')


'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p27.py ==========
Made a list of 65 letters
['A', 'D', 'E', 'A', 'E', 'C', 'F', 'E', 'D', 'A', 'A', 'A', 'F', 'A', 'A', 'A', 'F', 'B', 'E', 'F', 'E', 'B', 'E', 'B', 'C', 'D', 'C', 'B', 'C', 'B', 'A', 'F', 'D', 'A', 'D', 'F', 'D', 'B', 'C', 'D', 'E', 'C', 'C', 'B', 'D', 'C', 'E', 'A', 'C', 'B', 'E', 'E', 'D', 'E', 'B', 'F', 'C', 'B', 'D', 'A', 'A', 'A', 'A', 'B', 'C']
The letter "B" appears 11 time(s)
'''

