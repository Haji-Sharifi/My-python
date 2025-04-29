# Shopping cart program

food = []
prices = []
total = 0
while True:
    food = input("Enter the food item (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    else :
        price = float(input(f"Enter the price of {food}: "))
        prices.append(price)
        total += price
        print(f"{food} added to cart. Current total: ${total:.2f}")