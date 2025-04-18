# collection = single 'variable' used to store multiple values 
#   List     = []   - ordered and changeable. Duplicates OK
#   set      = {}   - unordered and immutable, but Add/Remove OK. No duplicates
#  Tuple     = ()   - ordered and unchangeable. Duplicates OK Faster 

fruits = ['apple', 'banana', 'cherry']
# print(dir(fruits))
# print(help(fruits))

# print(len(fruits))


# print("apple" in fruits) # True
# print("pinapple" not in fruits) # False

fruits[0] = "pinapple"


# print(dir(fruits))
for fruit in fruits:
   print(fruits)

