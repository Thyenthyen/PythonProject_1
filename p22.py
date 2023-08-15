# Program name: p22
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/4/2022
# Description:
'''
Write a Dice Game program that generates two random dice values between 1 and 6
for you, and 2 for the computer.
You get to roll as many times as you like (if you don't like your 2 dice), while
the computer only rolls once, after you have decided that you like your two dice. 
Determine who wins, you or the computer.
'''

print('Beat the coputer!')
      
from random import randint
      
while(True): #loop goes on forever.
    d1 = randint(1,6)
    d2 = randint(1,6)
    #userTotal = d1 + d2
    print('You rolled a %i and a %i (total = %i)' %(d1,d2,d1+d2))
    keep = input('Do you want to keep those?(y or n)')
    if keep != 'y':
          print('Rolling again...')
    if keep == 'y':
        break # until the user enter 'y'.

pc1 = randint(1,6)
pc2 = randint(1,6)
print('The computer rolled a %i and a %i (total = %i)' %(pc1,pc2,pc1+pc2))

#check winner
if pc1+pc2 > d1+d2:
    print('So sorry. You lose.')
elif d1+d2 > pc1+pc2:
    print('You win!')
else:
    print("It's a tie.")


'''
Beat the coputer!
You rolled a 5 and a 6 (total = 11)
Do you want to keep those?(y or n)n
Rolling again...
You rolled a 4 and a 5 (total = 9)
Do you want to keep those?(y or n)n
Rolling again...
You rolled a 3 and a 5 (total = 8)
Do you want to keep those?(y or n)y
The computer rolled a 2 and a 2 (total = 4)
You win!
'''
