# This is my first python code 

print("My name is Mustafa Sharifi")
print('I am a front-end-dev')

# Variable = A container for a value (string, integer,,float, boolean)
#            A variable behaves as if it was the value it contains

# Strings


firstName = 'Mustafa'
food = "pizza"
email = "example.com"

print(firstName)

print(f"Hello {firstName}")
print(f"U like {food}")
print(f"your emial is {email}")

#Integers

age = 21
quantity = 3
numOfStudents = 30

print(f"you are {age} years old")
print(f"you are buying {quantity} items")
print(f"you class has {numOfStudents} students")

#float

price = 10.99
gpa =3.2
distance =5.5


print(f"the price is ${price}")
print(f"your GPA is {gpa}")
print(f"you ran {distance}")

# Boolean

isStudent = True
isGraduate = False

print(f"are you a Student: {isStudent}")
print(f"are you graduated: {isGraduate}")


if isStudent:
    print('welcome')
else :
    print("go and register")



if isGraduate:
    print("Congratulations!")
else:
    print("You have classes to finish.")
