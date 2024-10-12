################################## Ithu vanthu   small letter la ulla tha captial ah letter change pannum
'''
name = 'abcd'

letter = name[0]  #a                                                                       ############  Only 0 na  (a mattum ) captial marum
ascii_value = ord(letter) #97
ascii_value = ascii_value - 32  #65
print(chr(ascii_value))



print()

'''


name = 'abcd123'        #################doubt

i=0  #a
while i<len(name):
    a= ord(name[i]) #97
    a=(a-32)                                                  ########## All letter change captial
    print(chr(a),end="")
    i+=1
print()

'''

name = 'akilajayb'

i=0  #a
while i<len(name):
    if i%2!=0:
        a= ord(name[i]) #97                                                                           ################ Only odd number change captial
        a=(a-32)
        print(chr(a),end="")
    else:
        print(name[i],end="")
    i+=1

'''


