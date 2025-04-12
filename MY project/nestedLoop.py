# nested loop = A loop within another loop (outer , inner)
#               outer looop :
#                    inner loop : 

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of column: "))

for i in range(3):
    for j in range(1, 10) :
        print(j, end=' ')
    print()