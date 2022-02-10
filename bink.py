import csv
from operator import itemgetter
from datetime import datetime
import time
import unittest
#1a
file = open("Python Developer Test Dataset.csv")
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
for i in rows:
    i[10]=float(i[10])
    if i[6].__contains__("Everything"):
        i[6]="EE"
    elif i[6].__contains__("Vodafone"):
        i[6]="Vodafone"
    elif i[6].__contains__("Arqiva"):
        i[6]="Arqiva"

sortedByRent = sorted(rows, key=itemgetter(10))
print("The list sorted by Current Rent in ascending order:\n")
print(sortedByRent)
print('\n')
#unit test 1a
#check if highest value is the last value unit test
assert sortedByRent[-1][10] == 28327.09


#1b
print("The first 5 items in the list:\n")
print(sortedByRent[:5])
print('\n')
#unit test 1b
#check if the length of the first 5 from the sortedbyrent array is eual to 5
assert len(sortedByRent[:5]) == 5


#2a
#making strings integers
for i in rows:
    i[9]=int(i[9])
#list comprehension
leaseYears25 = [i for i in rows if i[9]==25]
#data fields where lease years = 25
print("The list entries where Lease Years is equal to 25:\n")
print(leaseYears25)
print('\n')
#unite test 2a
#check if the lease years are 25
h = input("Choose a value from 0.." +str(len(leaseYears25))+" to assert whether the list comprehension executed succesfully and all the lease years are equal to 25. The script should continue & will not throw any errors if it is correct\n")
assert leaseYears25[int(h)][9] == 25


#2b
totalrent25 = [i[10] for i in leaseYears25]
print("The total rent for all items in the list where lease years is equal to 25:\n")
print(sum(totalrent25))
print('\n')
