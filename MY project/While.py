# While Loop = execute code WHILE some condation remain true

# name = input("Enter your name : ")

# while name == "" :
#     print("you did not enter your name")
#     name = input("Enter your name : ")

# print(f"Hello {name}")

# age = int(input("Enter your age : "))

# while age < 0 :
#     print("You age can not be negative")
#     age = int(input("Enter your age : "))

# print(f"Your age is {age}")


food = input("Enter your favorite food : (q to quit) ")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter your favorite food : (q to quit) ")

print("Goodbye")
