# Program name: p17
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/3/2022
# Description:
'''
Suppose that the tuition for a university is $10,000 this year and increases 5%
every year.
Write a program that computes the tuition in ten years and displays a table of
the years and tuition costs. A loop must be used.
'''

tuition = 10000
for year in range(1, 11, 1):
    print('Year %-3i'%year,'Tuition %1.f' %tuition )
    tuition += tuition*0.05

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p17.py ==========
Year 1   Tuition 10000
Year 2   Tuition 10500
Year 3   Tuition 11025
Year 4   Tuition 11576
Year 5   Tuition 12155
Year 6   Tuition 12763
Year 7   Tuition 13401
Year 8   Tuition 14071
Year 9   Tuition 14775
Year 10  Tuition 15513
'''
