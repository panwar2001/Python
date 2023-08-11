# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))
del(Dict[1]) 
print(Dict)

for key, value in Dict.items():
   print(key, '->', value)

Dict.clear()
