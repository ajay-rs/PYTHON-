'''
def add(no1, no2):
    round(no1/no2)
    return str(no1)+str(no2)

print(add(10,20))

print(round(add(10,20)))

===================================================================================

def shout(text): 
    return text.upper() 

print(shout('Hello')) 

yell = shout 

print(yell('Hello'))
=======================================================================================
def shout(text): 
    return text.upper() 

def whisper(text): 
    return text.lower() 

def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 

greet(shout) 
greet(whisper)

======================================================================================

def create_adder(x): 
    def adder(y): 
        return x+y 

    return adder 

add_15 = create_adder(15) 

print(add_15(10))
======================================================================================
'''
def decor_function(func):
    def display(name):
        if name == 'jesin':
            print("hello", name)
        else:
            func(name)
    return display


@decor_function
def wish(name):
    print("hi", name)


wish('jesin')
wish('kathir')
wish('mathi')
====================================================================================================
