# Program name: p43
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/8/2022
# Description:
'''
The function returns the sorted list in ascending
order if parameter 'reverse' is False.
The function returns the sorted list in descending
order if parameter 'reverse' is True.
Use the Bubble Sort inside of a function. 

Note: You are not allowed to use any built-in python
functions other than print() , input(), len() or range()
'''

def sort(alist,reverse):
    if reverse == False:
        #sorting in ascending order
        for j in range(0,len(alist),1):
            for i in range(0,len(alist)-1,1):
                if alist[i] > alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
        return alist
    if reverse == True:
        #sorting in descending order
        for j in range(0,len(alist),1):
            for i in range(0,len(alist)-1,1):
                if alist[i] < alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
        return alist

alist = [5,1,4,3,2]
print(sort(alist,False))
print(sort(alist,True))

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p43.py ==========
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
'''
