# Program name: p14
# Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/3/2022
# Description:
'''
Write a program that asks the user for day and month of a birthday.
The program then tells the Zodiac signs that will be compatible with
that birthday.
'''


'''
Zodiac Signs:
Constellation	English Name		    Dates	
-Aries		The Ram			Mar. 21–Apr. 19	
-Taurus		The Bull		Apr. 20–May 20	
-Gemini		The Twins		May 21–June 21	
-Cancer		The Crab		June 22–July 22	
-Leo		The Lion		July 23–Aug. 22	
-Virgo		The Virgin		Aug. 23–Sept. 22	
-Libra		The Balance	        Sept. 23–Oct. 23	
-Scorpio	The Scorpion	        Oct. 24–Nov. 21	
-Sagittarius	The Archer		Nov. 22–Dec. 21	
-Capricorn	The Goat		Dec. 22–Jan. 19	
-Aquarius	The Water Bearer        Jan. 20–Feb. 18	
-Pisces		The Fishes	        Feb. 19–Mar. 20
'''

day = int(input('Please enter day of birth:'))
month = int(input('Please enter month of birth:'))

if(month==3 and day>=21 and day<=31) or (month==4 and day>=1 and day<=19):
    print('You are Aries.')
    
elif(month==4 and day>=20 and day<=30) or (month==5 and day>=1 and day<=20):
    print('You are Taurus.')
    
elif(month==5 and day>=21 and day<=31) or (month==6 and day>=1 and day<=21):
    print('You are Gemini.')
    
elif(month==6 and day>=22 and day<=30) or (month==7 and day>=1 and day<=22):
    print('You are Cancer.')
    
elif(month==7 and day>=23 and day<=31) or (month==8 and day>=1 and day<=22):
    print('You are Leo.')
    
elif(month==8 and day>=23 and day<=31) or (month==9 and day>=1 and day<=22):
    print('You are Virgo.')
    
elif(month==9 and day>=23 and day<=30) or (month==10 and day>=1 and day<=23):
    print('You are Libra.')
    
elif(month==10 and day>=24 and day<=31) or (month==11 and day>=1 and day<=21):
    print('You are Scorpio.')
    
elif(month==11 and day>=22 and day<=30) or (month==12 and day>=1 and day<=21):
    print('You are Sagittarius.')
    
elif(month==12 and day>=22 and day<=31) or (month==1 and day>=1 and day<=19):
    print('You are Capricorn.')
    
elif(month==1 and day>=20 and day<=31) or (month==2 and day>=1 and day<=18):
    print('You are Aquarius.')
    
elif(month==2 and day>=19 and day<=29) or (month==3 and day>=1 and day<=20):
    print('You are Pisces.')
else:
    print('You enter invalid number.')


'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p14.py ==========
Please enter day of birth:31
Please enter month of birth:12
You are Capricorn.
'''




