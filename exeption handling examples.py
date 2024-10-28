try:
    no1 = int(input("Enter no. "))
    no2 = int(input("Enter no. "))
    print(no1/no2)
except ZeroDivisionError:
    print("Please check no2 ")
except ValueError:
    print("Inputs should be numbers")
print("Hi")
======================================
try:
    no1 = int(input("Enter no. "))
    no2 = int(input("Enter no. "))
    print(no1/no2)
except ZeroDivisionError:
    print("Please check no2 ")
    no2 = int(input("Enter no. "))
    print(no1/no2)
except ValueError:
    print("Inputs should be numbers")
print("Hi")
=======================================
try:
    no1 = int(input("Enter no. "))
    no2 = int(input("Enter no. "))
    l = (100,200)
    l[0] = 10
    print(l)
    print(no1/no2)
except ZeroDivisionError:
    print("Please check no2 ")
    no2 = int(input("Enter no. "))
    print(no1/no2)
except ValueError:
    print("Inputs should be numbers")
except TypeError:
    print("tuples cannot be reassigned")
print("Hi")
=========================================
try:
    no1 = int(input("Enter no. "))
    no2 = int(input("Enter no. "))
    l = [100,200]
    l[0] = 10
    print(l)
    d = dict()
    del d[0]
    print(no1/no2)
except ZeroDivisionError:
    print("Please check no2 ")
    no2 = int(input("Enter no. "))
    print(no1/no2)
except ValueError:
    print("Inputs should be numbers")
except TypeError:
    print("tuples cannot be reassigned")
except KeyError:
    print("Check dictionary")
except: 
    print("Call me")
print("Hi")
=============================================
try:
    no1 = int(input("Enter no. "))
    no2 = int(input("Enter no. "))
    l = [100,200]
    l[0] = 10
    print(l)
    d = dict()
    del d[0]
    print(no1/no2)
except: 
    print("Call me")
print("Hi")
=============================================
#traceback module
import traceback
try:
    no = int(input())
except:
    traceback.print_exc()           #error show pannum aprm stop agathu print

print("Hi")
============================================
