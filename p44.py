# Program name: p44
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/8/2022
# Description:
'''
You have 1000 lockers and 1000 students. All lockers are initially locked.

1st student opens all lockers

2nd student closes every other locker

3rd student opens(if closed) or closes (if open) every 3rd locker

4th student opens(if closed) or closes (if open) every 4th locker

1000th student opens(if closed) or closes (if open) every 1000th locker

Write a program to determine which exact locker numbers are open, and total
number that are open.

You are not allowed to use Python function  count()!!
'''
locker = [] #make empty list for locker (1 is locked and 0 is for opened)
#All lockers are initially locked
for i in range(0,1000,1):
    locker.append(1)#fill the list with 1


#1st student opens all lockers
for i in range(0,1000,1):
    locker[i] = 0 # open all lockers, flip 1 to 0

#2nd student closes every other lockers (like 0,2,4 or 1,3,5)
for i in range(0,1000,2):# every other locker
    locker[i] = 1 #close

#3rd student
#start from 3rd student, the loop with be the same condition to 1000th student
# get student number as a variable
for j in range(3,1001,1):
    for i in range(0,1000,j):
        if locker[i]==0:#if it's open,lock it
            locker[i]=1
        elif locker[i]==1:# otherwise, if it's locked,open it
            locker[i]=0
            
#look for opened locker
count = 0
for i in range(0,1000,1):
    if locker[i] == 0:
        print('locker',i,'is opened')
        count += 1
print('There are',count,'lockers open')

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p44.py ==========
locker 1 is opened
locker 4 is opened
locker 9 is opened
locker 16 is opened
locker 25 is opened
locker 36 is opened
locker 49 is opened
locker 64 is opened
locker 81 is opened
locker 100 is opened
locker 121 is opened
locker 144 is opened
locker 169 is opened
locker 196 is opened
locker 225 is opened
locker 256 is opened
locker 289 is opened
locker 324 is opened
locker 361 is opened
locker 400 is opened
locker 441 is opened
locker 484 is opened
locker 529 is opened
locker 576 is opened
locker 625 is opened
locker 676 is opened
locker 729 is opened
locker 784 is opened
locker 841 is opened
locker 900 is opened
locker 961 is opened
There are 31 lockers open
'''
    
    
    
