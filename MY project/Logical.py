# Logical Operators = evaluate mutiple conditions (or, and , not)
#                     or = at leat one condition is true
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)


# OR operation 
# temp = 20
# isRaining = True

# if temp > 35 or temp < 0 or isRaining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")


# AND operation

# temp = 20
# isSunny = True

# if temp > 28 and isSunny:
#     print("is hot Outside")
#     print("it is sunny")
# elif temp <= 0 and isSunny:
#     print("it is cold Outside")
#     print("it is sunny")
# elif temp < 28 and temp > 0 and isSunny:
#     print("it is warm Outside")
#     print("it is sunny")
# else :
#     print("it is cold Outside ")

# NOt Operation 

temp = 28
isSunny = False

if not (temp <= 28 or not isSunny):  
    print("It is hot outside")
    print("It is sunny")
elif not (temp > 0 or not isSunny):  
    print("It is cold outside")
    print("It is sunny")
elif not (temp >= 28 or temp <= 0 or not isSunny):  
    print("It is warm outside")
    print("It is sunny")
else:
    print("It is cold outside")


