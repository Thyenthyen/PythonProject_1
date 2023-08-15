# Program name: p46
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/13/2022
# Description:
'''
Write a Python program to do the following:

1.Let the user enter a file name (such as "myMovies.txt").
2.Let the user enter the titles of 4 of their favorite movies using a loop.
3.Write using a loop the 4 movie titles to a file,one per line,and closes the file.
4.Read the 4 movie titles from "myMovies.txt" using splitlines(), stores them in a
list, and then shows the list.
5.Write the titles in reverse order into a file "reverseOrder.txt"
'''

#creat a file base on user input
fileName = input('Please enter a file name:')
newFile = open(fileName,'w')#make afile named after user input
                        #^ means open file to write over on the the file if it has sth in it already
for i in range(1,5,1):
    movie = input('Enter a movie title' +' %i:' %i )
    newFile.write(movie + '\n') #write on the file
newFile.close()# close the file


newFile = open(fileName, 'r') # 'r' means open file to read from the file
fileListOfLines = newFile.read().splitline() # slit each line in that file
                          #^^ read the file
newFile.close()

newFile = open('reverseOrder.txt', 'w')
for i in range(len(fileListOfLines)-1,-1, -1): # -1, for reverse order
    newFile.write(fileListOfLines[i] + '\n')
newFile.close()

'''
========== RESTART: C:/Users/Thyen/OneDrive/Máy tính/python hw/p46.py ==========
Please enter a file name:myMovies.txt
Enter a movie title 1:movie1
Enter a movie title 2:movie2
Enter a movie title 3:movie3
Enter a movie title 4:movie4
'''
     
