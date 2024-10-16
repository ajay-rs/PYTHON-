#Left side:keys ,Right side:value pair
d = {"chicken":110, "mutton":150, "egg":100, "plain":100}
print(d)






#Name(key) and rollno(valuepair) 
students = {}
count = int(input("Enter no. of students: "))
for i in range(count):
    name = input("Enter Name: ")
    roll_no = int(input("Enter Roll no. "))
    students[name] = roll_no

print(students)
print(students.keys())
print(students.values())




#
fruits = {"banana":100, "apple":200, "orange":220}
total = 0
for fruit_price in fruits.values(): 
    total = total + fruit_price

print(total)



#
fruits = {"banana":100, "apple":200, "orange":220}
total = 0
for fruit_price in fruits.values(): 
    fruit_name = input("What fruit you bought: ")
    total = total + fruits[fruit_name]

print(total)


fruits = {"banana":100, "apple":200, "orange":220}
total = 0
for fruit_price in fruits.values(): 
    fruit_name = input("What fruit you bought: ")
    total = total + fruits.get(fruit_name)

print(total)
