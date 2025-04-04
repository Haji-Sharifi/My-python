import time

myTime = int(input('Enter the time in seconds: '))


for x in range (0 , myTime):
    print(x)
    time.sleep(1)


print("time's up")
