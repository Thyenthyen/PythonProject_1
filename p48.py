# Program name: p48
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/13/2022
# Description:
'''
Write a program which reads the data from file sunspots.txt
...and computes the average for each year, writing them one per line
to a file averages.txt
'''

myFile = open('sunspots.txt','r')
fileAsListOfLines = myFile.read().splitlines()
myFile.close()

otherFile = open('averages.txt','w')
otherFile.write('Year  Average\n')

for j in range (0,len(fileAsListOfLines),1):
    aLine = fileAsListOfLines[j]

    lineData = aLine.split()

    year = lineData[0]

    sumData = 0

    for i in range(1, len(lineData),1):#start with 1 bc we dont want 0 which is the year
        sumData += float(lineData[i])
    avg = sumData/(len(lineData)-1)# not include the year part
    otherFile.write('%s  %.2f\n' %(year,avg))
    
otherFile.close()

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p48.py ==========

'''
