# Shopping cart program

foods = []
prices = []
total = 0
while True:
    food = input("Enter the food item (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    else :
        price = float(input(f"Enter the price of {food}: $ "))
        foods.append(food)
        prices.append(price)

print("------ Your Shopping Cart ------")

for food in food
    print(food)