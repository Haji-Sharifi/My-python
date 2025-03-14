# if = Do some code IF some condition is True
#      Else do something else

# age = int(input('Enter your age : '))

# if age >= 100 :
#     print('you are too old to be signed up')
# elif age >= 18 :
#     print('You are now signed up')
# elif age < 0:
#     print("you haven't even born yet ")
# else :
#     print('You must be at least 18 years old')


response = input("Would you like food (Y/N)?: ").strip().upper()

if response == "Y":
    print("What would you like to order?")
    order = input("We have Pizza, Burger, Sandwich, and Chicken Wings: ").strip().upper()
    
    if order == "PIZZA":
        print("Your pizza order has been placed!")
    elif order == "BURGER":
        print("Your burger order has been placed!")
    elif order == "SANDWICH":
        print("Your sandwich order has been placed!")
    elif order == "CHICKEN WINGS":
        print("Your chicken wings order has been placed!")
    else:
        print("Sorry, we don't have that item.")
        
elif response == "N":
    print("Thanks for visiting! Have a great day.")
else:
    print("Invalid input. Please enter Y or N.")


# if response == "yes" or response == "umm":
#     print("so lets eat some food ")
# else :
#     print("okey than")
