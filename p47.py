# Program name: p47
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/13/2022
# Description:
'''
Write a program which :

Writes a random number (50 to 55) of numbers (0 to 100) in a file
Opens the file and reads the numbers from it into a list
Sorts the list and Shows it.
Calculates the median.
Note: You may NOT use the Python built in functions: sort(),
sorted(), sum(), median()
'''

from random import randint

totalNum = randint(50,55)
newFile = open('randomNum.txt','w')
for i in range(0,totalNum,1):
    newFile.write(str(randint(0,100)) + '\n')
newFile.close()

newFile = open('randomNum.txt', 'r')
fileAsLineList = newFile.read().splitlines() #splitlines() is split lines for 'open'

for i in range(0,len(fileAsLineList)-1,1):
    for j in range(0,len(fileAsLineList)-1,1):
        if int(fileAsLineList[j]) > int(fileAsLineList[j+1]): # change he numbers from the file which are strings into integers
               temp = fileAsLineList[j]
               fileAsLineList[j] = fileAsLineList[j+1]
               fileAsLineList[j+1] = temp

print(fileAsLineList)

# find the index of meadian if we have odd total numbers
if len(fileAsLineList)%2 != 0:
    medianIndex = int(len(fileAsLineList)/2)
    median = fileAsLineList[medianIndex]
    print('median for odd total:',median )

#fins the index of median if we have even total numbers
else:
    medianIndex2 = int(len(fileAsLineList)/2)
    medianIndex1 = medianIndex2 - 1
    median =(int(fileAsLineList[medianIndex1]) + int(fileAsLineList[medianIndex2]))/2
    print('median for even total:', median)
                   
'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p47.py ==========
['1', '2', '3', '4', '4', '5', '5', '5', '7', '14', '15', '19', '20', '20', '28', '29', '30', '30', '32', '39', '42', '42', '47', '51', '51', '52', '52', '54', '54', '55', '56', '58', '58', '61', '65', '65', '68', '71', '76', '77', '78', '80', '83', '83', '84', '87', '88', '89', '90', '91', '91', '95', '97', '98']
median for even total: 53.0

========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p47.py ==========
['0', '2', '2', '3', '4', '6', '7', '10', '13', '14', '15', '16', '16', '24', '27', '29', '29', '29', '30', '30', '31', '32', '35', '36', '36', '37', '46', '51', '52', '53', '56', '61', '65', '66', '66', '67', '72', '73', '75', '76', '77', '81', '86', '87', '87', '87', '88', '89', '90', '91', '98', '99', '100']
median for odd total: 46
'''



