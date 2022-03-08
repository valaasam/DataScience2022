#!/usr/bin/python3

#### HW3 Question 2 ####

#### A.

print("PART A")

#Create a list of numbers (any numbers you like). 
numbers=list(range(0,109,10))

#check if this worked
print(numbers)

#loop through the items in the list adding 1 to every number
#for each item in my list (numbers), add 1
new_numbers = [x+1 for x in numbers]

#print those numbers.
print(new_numbers)


####

print("")

#### B.

print("PART B")

#Creae a dictionary of animals and their sizes
animal_size_dict={
    'ant':0.5,
    'bird':4,
    'cat':6,
    'frog':2,
    'dinosaur':700,
    'trevor':21,
}

#print keys of dictionary
print(animal_size_dict.keys())

#make list of animal names & print to see it worked
animal_list=list(animal_size_dict.keys())
print(animal_list)

#if else statement to print out the animal name and the word “big” if the weight is over 20 grams 
#and the word “small” if the weight is less than 20 grams.

for item in animal_list:
    if animal_size_dict[item]>20:
        print("%s: big" %item)
    else: print("%s: small"%item)
