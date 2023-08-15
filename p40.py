# Program name: p40
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/8/2022
# Description:
'''
Ask the user to enter X numbers into a list. Calculate
and show the sum, average, min, max of those numbers.

Note: You are not allowed to use any pre-existing python
functions such as sample(), sum(), min(), max(), average(),
sort(), sorted()!!!...unless you write them yourself.
'''

aList = []
enter = int(input('How many numbers would you like to enter?'))
for e in range(0,enter,1):
    num = int(input('Enter number %i :' %(e+1)))
    aList.append(num)

#fing the smallest
smallest = aList[0]
for a in range(1,len(aList),1):
    if aList[a] < smallest:
        smallest = aList[a]

#fing the largest
largest = aList[0]
for b in range(1,len(aList),1):
    if aList[b] > largest:
        largest = aList[b]

#fing the sum
sum = 0
for c in range(0,len(aList),1):
    sum += aList[c]

#find the avg
avg = sum / len(aList)


print('List:',aList)
print('Sum =',sum)
print('Average =',sum,'/',enter,'= %.1f' %avg)
print('Largest =',largest)
print('Smallest =',smallest)


'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p40.py ==========
How many numbers would you like to enter?11
Enter number 1 :26
Enter number 2 :23
Enter number 3 :48
Enter number 4 :32
Enter number 5 :44
Enter number 6 :21
Enter number 7 :32
Enter number 8 :20
Enter number 9 :49
Enter number 10 :48
Enter number 11 :34
List: [26, 23, 48, 32, 44, 21, 32, 20, 49, 48, 34]
Sum = 377
Average = 377 / 11 = 34.3
Largest = 49
Smallest = 20
'''
