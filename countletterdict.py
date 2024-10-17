'''
name = 'piriankumar'
d = dict()

for letter in name: 
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] = d.get(letter)+1
else:
    print(d)
'''







people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

for details_dict in people.values():
    for key, value in details_dict.items():
        if value=='27':
            print(details_dict['name'])

