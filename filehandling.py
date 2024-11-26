'''
f = open("libin.txt","w")

f.write("Ajay\n")

f.write("Akil\n")

f.write("jesin\n")

f.write("7092514027")

f.close()


f = open("libin.txt","r")

l = f.read()

print(l)

f.close()

'''
f = open("libin.txt","r")
lines = f.readlines()

count=1
for line in lines:
    if line ==" ":
        count=count+1
        print(count, end='')
f.close()

'''
#No. of letters in a given text file
f = open("libin.txt","r")
lines = f.readlines()

for name in lines:
    if name[0] =="A":
        print(name)

f.close()


f = open("libin.txt","r")
lines = f.readlines()

for name in lines:
    if 'ay'in name:
        print(name)

f.close()

f = open("libin.txt","r")
lines = f.readlines()

for name in lines:
    if name.isnumeric():
            print(name)

f.close()



f= open("libin.txt","r")  
print(f.tell())
print(f.read(10))
print(f.tell())
f.close()

#import module
import os, sys
file_name = input("Enter File Name: ")
if os.path.isfile(file_name):
    print("File is present")
    with open(file_name, "r") as f:
        print(f.read())




#comma sparated value   (python la csv file excel sheet read panna tha csv module use pannurom )
# ithu write panna ...
import csv
with open("student.csv","w") as f:
    pen = csv.writer(f)
    pen.writerow(["StudId", "Name", "Address"])
    stud_id = int(input("Enter no. "))
    name = input("Enter name ")
    address = input("Enter Address: ")
    pen.writerow([stud_id, name, address])


import csv
with open("student.csv","r") as f:
    book = csv.reader(f)
    l = list(book)
    for line in l:
        for cell in line:
            print(cell, end=' ')
    




#count the number of lines
f = open("libin.txt","r")
lines = f.readlines())
for i in len(lines):
    
print()

'''








