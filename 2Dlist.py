# fruits =     ["apple", "orange", "banana", "coconut"]
# vegtabeles = ["celery", "carrots", "potatoes"]
# meats =      ["checken" , "fish" , "turkey"]

# groceries =  [fruits, vegtabeles, meats]

# # fruits[0] = "kiwi"
# # print(fruits)

# print(groceries[0][0])
# print(groceries[1][2])


groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["checken" , "fish" , "turkey"]]

for collection in groceries :
    for food in collection :
        print(food, end=" ")
    print()