#index start from 0(A=0,j=1,A=2,Y=3)
name = "AJAY"


i = 0  #Appo  i means (index)
while i<len(name):            #len means ajay full name (3 vidu 0 kamina run aagu) aprm stop.............(Ithu vara string ah tha irukum)
    ascii_value = ord(name[i])                         #asciivale oru variable create panni ...............Encryption ku(ord) nu oru name use panni atha decimal ah irukum appo(integer ah agum))
    ascii_value = ascii_value + 1                                           #(variable la store panni atha 2 or 1  add kudkanum  (athu deximal la poi pakkum Aprm add pannum))  (ippo integer ah irukum)
    print(chr(ascii_value),end='')                                                #(Appo atha( chr )nu oru name kudutha atha string ah change agum)
    i+=1





'''

name="AJAY"

i=0
while i<len(name):
    print(chr(ord(name[i])+1),end='')                            #advanced
    i=i+1
'''
