# Python Compound intrest claculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount : "))
    if principle <= 0:
        print("Principle amount can not be negative or zero")

while rate <= 0:
    rate = float(input("Enter the rate of intrest : "))
    if rate <= 0:
        print("Rate of intrest can not be negative or zero")
while time <= 0:
    time = float(input("Enter the time in years : "))
    if time <= 0:
        print("Time can not be negative or zero")


print(principle)
print(rate)
print(time)