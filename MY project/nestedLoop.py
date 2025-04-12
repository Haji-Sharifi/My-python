# nested loop = A loop within another loop (outer , inner)
#               outer looop :
#                    inner loop : 

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of column: "))
symbol = input("Enter the symbol you want to use: ")

for i in range(rows):
    for j in range(columns) :
        print(symbol, end=' ')
    print()