# import time

# myTime = int(input("Enter the time in seconds: "))

# for x in range(0 , myTime):
#     print(myTime - x)
#     time.sleep(1)

# print("Time's up!")


# import time 

# myTime = int(input("Enter the time in seconds: "))

# for x in reversed(range(0, myTime)):
#     print(x)
#     time.sleep(1)
# print("Time's up!")

import time 

myTime = int(input("Enter the time in seconds: "))

for x in range(myTime, 0, -1):
    seconds = x % 60 
    minutes = int(x / 60 ) % 60 
    hours = int(x / 3600) 
    print(f"{hours:02}{minutes:02}{seconds:02}")
    time.sleep(1)
print("Time's up!")
