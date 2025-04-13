# collection = single 'variable' used to store multiple values 
#   List     = []   - ordered and changeable. Duplicates OK
#   set      = {}   - unordered and immutable, but Add/Remove OK. No duplicates
#  Tuple     = ()   - ordered and unchangeable. Duplicates OK Faster 

fruits = ['apple', 'banana', 'cherry']

print(fruits[1])  # Output: banana
print(fruits[-1])  # Output: cherry
print(fruits[1:3])  # Output: ['banana', 'cherry']
print(fruits[1:])  # Output: ['banana', 'cherry']
print(fruits[:2])  # Output: ['apple', 'banana']
print(fruits[-2:])  # Output: ['banana', 'cherry']
print(fruits[-3:-1])  # Output: ['apple', 'banana']
print(fruits[-2:])  # Output: ['banana', 'cherry']   