#!/usr/bin/python3

#### HW3 Question 1 ####

### a. 

#assign number to 'num'
num='112345678911234566'

#count occurances of '2'
LEN=num.count('2')
print("occurences of 2 = %d" %LEN)

### b.

#assign phrase variable
phrase=input("Describe your favorite dog and what their name is: ")

#change to lowercase
newphrase=phrase.lower()

#remove spaces
newphrase=newphrase.replace(' ', '')

#print length
LEN2 = len(newphrase)
print('length of characters in phrase without spaces = %s' %LEN2)

