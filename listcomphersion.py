# Normal using list
l = ['libin','ajay','akil','joshua','sakthi'] 
for name in l:
    if name[0] == "a":
        print(name)                                        

#List comphersion
l = ['libin','ajay','akil','joshua','sakthi'] 
l1=[name for name in l if len(name) == 4]
print(l1)

