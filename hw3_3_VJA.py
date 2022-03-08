#!/usr/bin/python3

#### HW3 Question 3 ####

# Check working directory to make sure I am in "Part.3.PythonProgramming"
import os
os.getcwd()

#read in Bloom_etal file using pandas read_csv function
from pandas import read_csv
infile = read_csv('./Pandas/Bloom_etal_2018_Reduced_Dataset.csv')

#check that the file uploaded correctly
print(infile.head())
print("")

#for each line in the file, print out the taxa name and diandromous status
for i in infile.index: 
     print(infile["taxa"][i]+ ": "+ infile["Reg"][i])

print("")

#Add up all log body sizes and print total sum
print("sum of all log body sizes:")
print(infile.logbodysize.sum())

