

#
fruits = {"banana":100, "apple":200, "orange":220}
total = 0
for fruit_price in fruits.values(): 
    fruit_name = input("What fruit you bought: ")
    total = total + fruits[fruit_name]

print(total)


