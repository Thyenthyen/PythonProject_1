# Program name: p21
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/4/2022
# Description:
'''
Which of the below gives you more money?
1) A penny which doubles it's value every day over 30 days, or
2) A million dollars
Write a program which calculates exactly how much more (or less) you can make
with the penny on day 30. A loop must be used.
'''

penny = 1
dollarCase2 = 1000000
for day in range(1,31,1):
    dollar = penny/100
    print('The total money after day %2i' %day,'is %-9i'%penny,'=',dollar,'$.')
    penny = penny*2
if dollar>dollarCase2:
    dollar = dollar - dollarCase2
    print('Case 1 is more than case 2',dollar,'$')
if dollarCase2>dollar:
    dollar = dollarCase2 - dollar
    print('Case 1 is more than case 2',dollar,'$')

    
'''
The total money after day  1 is 1         = 0.01 $.
The total money after day  2 is 2         = 0.02 $.
The total money after day  3 is 4         = 0.04 $.
The total money after day  4 is 8         = 0.08 $.
The total money after day  5 is 16        = 0.16 $.
The total money after day  6 is 32        = 0.32 $.
The total money after day  7 is 64        = 0.64 $.
The total money after day  8 is 128       = 1.28 $.
The total money after day  9 is 256       = 2.56 $.
The total money after day 10 is 512       = 5.12 $.
The total money after day 11 is 1024      = 10.24 $.
The total money after day 12 is 2048      = 20.48 $.
The total money after day 13 is 4096      = 40.96 $.
The total money after day 14 is 8192      = 81.92 $.
The total money after day 15 is 16384     = 163.84 $.
The total money after day 16 is 32768     = 327.68 $.
The total money after day 17 is 65536     = 655.36 $.
The total money after day 18 is 131072    = 1310.72 $.
The total money after day 19 is 262144    = 2621.44 $.
The total money after day 20 is 524288    = 5242.88 $.
The total money after day 21 is 1048576   = 10485.76 $.
The total money after day 22 is 2097152   = 20971.52 $.
The total money after day 23 is 4194304   = 41943.04 $.
The total money after day 24 is 8388608   = 83886.08 $.
The total money after day 25 is 16777216  = 167772.16 $.
The total money after day 26 is 33554432  = 335544.32 $.
The total money after day 27 is 67108864  = 671088.64 $.
The total money after day 28 is 134217728 = 1342177.28 $.
The total money after day 29 is 268435456 = 2684354.56 $.
The total money after day 30 is 536870912 = 5368709.12 $.
Case 1 is more than case 2 4368709.12 $
'''
