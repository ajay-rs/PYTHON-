'''
# logic 
fruits = ['apple', 'banana', 'grapes', 'papaya']
for i in fruits:
    if len (i) == 6:
        print (i)  

#fliter
fruits = ['apple', 'banana', 'grapes', 'papaya']
resultlist = list(filter(lambda  i:len(i)==6,fruits))
print(resultlist)
===================================================================
'''
'''
#logic
names = ['sakthi', 'ajay', 'joshua', 'jecin']                         
for i in names:
    if i[0] =='j':
        print(i)
        

#fliter
names = ['sakthi', 'ajay', 'joshua', 'jecin']

def find_j_names(name):
    return name[0] == 'j'

result = lambda name: name[0] == 'j'

j_names = list(filter(result, names))
print(j_names)

===================================================================
'''
'''
names = ['sakthi', 'ajay', 'joshua', 'jecin']

#lambda name:name for letter in name if letter == 'j'
              
result = lambda name: 'j' in name

j_names = list(filter(result, names))
print(j_names)

===================================================================
'''
'''
l1 = [10,15,20,25,30]
l2 = [5,10,15,20,30,40,50]

result = list(filter(lambda no:no[0] %10==0 and no[1]%10==0, 
            zip(l1,l2)))
print(result)
''
'
