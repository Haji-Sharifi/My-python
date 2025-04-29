# collection = single 'variable' used to store multiple values 
#   List     = []   - ordered and changeable. Duplicates OK
#   set      = {}   - unordered and immutable, but Add/Remove OK. No duplicates
#  Tuple     = ()   - ordered and unchangeable. Duplicates OK Faster 

# fruits = ['apple', 'banana', 'cherry', 'orange', ]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))


# print("apple" in fruits) # True
# print("pinapple" not in fruits) # False

# fruits[1] = "pinapple"
# fruits.append("pinapple") # add to the end
# fruits.remove("banana") # remove by value
# fruits.insert(0, 'pinapple') 
# fruits.sort()
# fruits.reverse()
# fruits.index('apple') # find index of value
# fruits.clear() # remove all items

# print(fruits.index('apple')) # find index of value
# print(fruits.count('apple')) # count how many times a value appears


# print(dir(fruits))
# for fruit in fruits:
#    print(fruit)

#  using set {}

# fruits = {'apple', 'banana', 'cherry', 'orange', }

# print('pineapple' in fruits) # False

# print(fruits[0]) # TypeError: 'set' object is not subscriptable



# using Tuple 

fruits = ('apple', 'banana', 'cherry', 'orange', )
 
print (fruits.count('apple')) # count how many times a value appears

for fruit in fruits:
    print(fruit)

# print("Pineapple" in fruits)
