# Conditional expression = A one-line shortcut for the if-else (ternary Operator)
#                          Print ot assign one of two values based on a condation 
#                          X if condation else Y

num = 6
a = 6
b = 7
age = 22
temperature = 30
userRole = "guest"


# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "Odd"
# maxNum = a if a > b else b
# minNum = a if a < b else b
# weather = "hot" if temperature > 20 else "cold"
# status = "Adult" if age >= 18 else "child"
accessLevel = "Full Access" if userRole == "Admin" else "limited Access"


print(userRole)

