# Program name: p38
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/8/2022
# Description:
'''
Write a program that asks the user to enter a sentence.

The program then finds the longest word in the sentence, and shows it.

Note: The use of python functions max() and sorted() is not permitted!
'''

sen = input('Please Enter a sentence:')
word = sen.split()

#make longest equal to first word
longest = word[0]
for i in range(1,len(word),1):
    if len(word[i]) > len(longest):
        longest = word[i]

print('The longest word is "', longest,'" has',len(longest),'character.')


'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p38.py ==========
Please Enter a sentence:Sunday rain is falling
The longest word is " falling " has 7 character.
'''
