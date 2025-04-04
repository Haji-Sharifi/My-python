# For loops = execute a block of code a fixed number of times 
#             You can iterate over a range, string, sequence, etc.
# Syntax: for x in range(0,10):
#                 print(x)


# for x in range(1, 11):
#     print(x)
    
# The range function generates a sequence of numbers from 1 to 11



# for x in reversed(range(1, 11)):
#     print(x)

# it will print the numbers from 10 to 1
# The reversed function reverses the order of the sequence

for x in range(1, 11 ,2) :
    print(x)
# it will print the odd numbers from 1 to 10

creditCard = "1234-5678-9012-3456"
for x in creditCard:
    print(x)    # this will loop over the string 

for x in range(1, 21) :
    if x == 13 :
        continue  # if we use break the loop will be stoped
    else :
        print(x)