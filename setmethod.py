# Add method
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s1.add(25)
print(s1)
print(s2)


#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y) 

print(x)

#remove
s1 = {10,20,30,40,25}
s2 = {30,40,50,60}
s1.remove(25)
print(s1)
print(s2)


#union
s1 = {10,20,30,40}
s2 = {40,50,60,70}
print(s1.union(s2))

#intersection
s1 = {10,20,30,40}
s2 = {40,50,60,70}
print(s1.intersection(s2))

#difference
s1 = {10,20,30,40}
s2 = {40,50,60,70}
print(s1.difference(s2))

#symmetric difference
s1 = {10,20,30,40}
s2 = {40,50,60,70}
print(s1.symmetric_difference(s2))
