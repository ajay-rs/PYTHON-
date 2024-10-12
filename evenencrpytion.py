###############ithu epdi na even number varathu mattum name(letter) change pannum...........

name = "LIBIN"



i = 0
while i<len(name):
    if i%2==0:
        a = ord(name[i])                    ###############################ithu even value mattum change aagum        (==)
        a = a + 3
        print(chr(a),end='')
    else:
        print(name[i],end='')
    i+=1






'''
name = "LIBIN"

print(name)

i = 0
while i<len(name):
    if i%2!=0:
        ascii_value = ord(name[i])                    ###############################3ithu odd value mattum change aagum       (!)
        ascii_value = ascii_value + 1
        print(chr(ascii_value),end='')
    else:
        print(name[i],end='')
    i+=1
'''


