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
