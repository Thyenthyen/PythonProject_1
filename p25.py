# Program name: p25
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/4/2022
# Description:
'''
Write a program that asks the user to input a sentence.
The program will ask the user what two letters are to be counted.
You must use a “for” loop to go through the sentence & count how
many times the chosen letter appears in the sentence.
'''

sen = input('Please enter a sentence:')
count1 = 0
count2 = 0
letter1 = input('Please enter letter 1:')
letter2 = input('Please enter letter 2:')

for index in range(0,len(sen),1):
    if(sen[index] == letter1):
        count1 += 1
    if(sen[index] == letter2):
        count2 += 1
        
print('The letter %s was found' %letter1,count1,'time(s).')
print('The letter %s was found' %letter1,count2,'time(s).')

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p25.py ==========
Please enter a sentence:HELLO MY WORLD
Please enter letter 1:H
Please enter letter 2:L
The letter H was found 1 time(s).
The letter H was found 3 time(s).
'''

    
    
    
    
    
    
