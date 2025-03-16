# Python weight converter 

weight = float(input("Enter Your Weight: "))
unit = input("Kilograms or Pounds? (k or l): ").lower()

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")
