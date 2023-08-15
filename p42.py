# Program name: p42
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/8/2022
# Description:
'''
Write the below 5 functions according to the following requirements:

sum (list_parameter) : returns the sum of numbers inside a list
average (list_parameter) : returns the average of numbers inside a list
min (list_parameter) : returns the smallest of all numbers inside a list
max (list_parameter) : returns the largest of all numbers inside a list
main () : calls all the other functions above
'''
def sum(aList):
    total = 0
    for i in range(0,len(aList),1):
        total += aList[i]
    return total
def minimum(aList):
    smallest = aList[0]
    for i in range(0,len(aList),1):
        if aList[i] < smallest:
            smallest = aList[i]
    return smallest
def maximum(aList):
    largest = aList[0]
    for i in range(0,len(aList),1):
        if aList[i] > largest:
            largest = aList[i]
    return largest
def average(aList):
    total = sum(aList)
    avg = total / len(aList)
    return avg
    

def main():
    aList = [1,2,3]
    print('The sum of',aList,'is',sum(aList))
    print('The min of',aList,'is',minimum(aList))
    print('The max of',aList,'is',maximum(aList))
    print('The average of',aList,'is',average(aList))
main()

'''
======== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/testing.py ========
The sum of [1, 2, 3] is 6
The min of [1, 2, 3] is 1
The max of [1, 2, 3] is 3
The average of [1, 2, 3] is 2.0
'''
