# format specifiers = {:flags} format a value based on what 
#                              flage are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate that many spaces
# :< = left justify
# :^ = center align
# :+ = use a plus sign to indicate positive value 
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1 = 3.14159
price2 = -987.65
price3 = 12.34


print(f"price 1 is {price1:.2f}")  #showing decimal point
print(f"price 2 is {price2}")
print(f"price 3 is {price3}")

      