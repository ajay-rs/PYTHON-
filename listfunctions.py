# append:
l1 = [10,20,30]
l2 = [40,50,60]
l1.append(l2)
print(l1)
print(l2)
print(len(l1))


# append:
l=[1,2,3,4]
l.append(5)
print(l)




# extend:
l1 = [10,20,30]
l2 = [40,50,60]
l1.extend(1)#40 50 60
print(l1)
print(len(l1))





#index:
Animals= ["cat", "dog", "tiger","dog"]
# searching positiion of dog
print(Animals.index("dog"))


#insert:
List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List.insert(2, 10087)
print(List)


#copy:
#shallow copy
import copy
a = [10,20,30]
b = copy.copy(a)



a[1] = 200
print(a[1])
print(b[1])
print(a)
print(b)


#deep copy
a = [10,20,30]
b = a
a[1]=2
print(a)
print(b)


#clear
lis = [1, 2, 3]
lis.clear()
print(lis)












