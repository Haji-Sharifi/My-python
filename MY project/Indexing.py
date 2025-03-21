# indexging = accessing elements of a sequence using [] (indexing operation)
#             [start : end : step]

# creditNumber = "1234-5678-9012-3456"

# print(creditNumber[0])

# print(creditNumber[0 : 4]) # using start :

# print(creditNumber[5 : 9])

# print(creditNumber[5 : ]) # using end :

# print(creditNumber[-1])

# print(creditNumber[::3]) # using step :

creditNumber = "1234-5678-9012-3456"

lastDegits = creditNumber[-4 : ]

print(f"XXXX-XXXX-XXXX-{lastDegits}")