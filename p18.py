# Program name: p18
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/3/2022
# Description:
'''
Write a program that displays the characters in the ASCII character table
from ! to ~.
Display ten characters per line.
The characters are separated by exactly one space.
'''
'''
print('a')
print(ord('a')) show 97, ascii for 'a'
print(chr(97)) show 'a', ascii 97 converted to charater a
'''


count = 0
for ascii in range(33,127,1):
    #print(ascii, ' ', end = '') end = means preventing a new line.
    print(chr(ascii), '', end = '')
    count += 1
    if count == 10:# as 10 chr per line.
        print()    # show a new line
        count = 0  # restart counting.



'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p18.py ==========
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
'''
