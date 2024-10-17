'''
price_dict = {'apple':100, 'pineapple':120, 'orange':110,'banana':100, 'lemon':150}
highest=0
for key,value in price_dict.items():
      if value > highest:
        highest=value
        k=key
else:
     print(key)
     print(highest)
'''



'''

#convert dict into list:
price_dict = {'apple':100, 'pineapple':120, 'orange':110,'banana':100, 'lemon':150}
print(list(price_dict))


'''



'''
price_dict = {'apple':100, 'pineapple':120, 'orange':110,'banana':100, 'lemon':150}
for fruit in price_dict:
    print(fruit, price_dict[fruit])
'''





'''

price_dict = {'apple':100, 'pineapple':120, 'orange':110,'banana':100, 'lemon':150}
for fruit in price_dict[:2]:
    print(fruit, price_dict[fruit])
'''
