# Program name: p39
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/8/2022
# Description:
'''
Write a program that asks the user to enter a sentence.
Your program will:
Show how many words are in the sentence 
Show the last word of the sentence
Ask the user to enter their own word, and count how many times their
word appears in the sentence
Note: you can't use the built-in python function count() to do this!
'''


sen = input('Please enter a sentence: ')
wordSen = sen.split()

print('There are', len(sen),'words in the sentence you entered') 
first = wordSen[0]#the first word of the sentence
last = wordSen[len(wordSen)-1]# get the last word of the sentence

print('The last word is "', last,'"')
word = input('Please enter a word to search:')
count = 0
for i in range(0, len(wordSen),1):
    if wordSen[i] == word:
        count += 1
print('The word "',word,'" appears',count,'time(s)')

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p39.py ==========
Please enter a sentence: the fox and the dog
There are 19 words in the sentence you entered
The last word is " dog "
Please enter a word to search:the
The word " the " appears 2 time(s)
'''

