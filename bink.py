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


#3a
tenantNameMasts = {}
tenantNameMasts['Cornerstone Telecommunications Infrastructure'] = Cornerstone=sum([i.count("Cornerstone Telecommunications Infrastructure") for i in rows])
tenantNameMasts['EE']=sum([i.count("EE") for i in rows])
tenantNameMasts['Arqiva']=sum([i.count("Arqiva") for i in rows])
tenantNameMasts['O2 (UK) Ltd']=sum([i.count("O2 (UK) Ltd") for i in rows])
tenantNameMasts['Vodafone']=Vodafone=sum([i.count("Vodafone") for i in rows])
print("Dictionary containing the Tenant Names & the count of masts in HRF: \n")
print(tenantNameMasts)
print('\n')


#4a
for i in rows:
    i[7]=datetime.strptime(i[7], "%d %b %Y").strftime("%d/%m/%Y")
    i[8]=datetime.strptime(i[8], "%d %b %Y").strftime("%d/%m/%Y")

#print(time.strptime(rows[0][7], "%d/%m/%Y") > )
leasestartdate = [i for i in rows if time.strptime(i[7], "%d/%m/%Y") < time.strptime("31/08/2007", "%d/%m/%Y") and time.strptime(i[7], "%d/%m/%Y") > time.strptime("01/06/1999", "%d/%m/%Y")]

print("The entries where the Lease Start Date fell between 1st June 1999 and 31st August 2007: \n")
print(leasestartdate)
print("\n")
