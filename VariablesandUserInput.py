print("This part takes two numbers from the user, and outputs their sum.")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
sum = float(num1) + float(num2)
print(" Sum of the entered numbers is: {}".format(sum))

print("This part takes two numbers from the user, and \
outputs the equation representing the multiplication of the two numbers.")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
multi = float(num1) * float(num2)
print("{} * {} = {}".format(num1, num2, multi))

print("This part takes a distance in kilometers from the user, \
and output the distance in meters and centimeters.")
dist = input("Enter a number for a distance: ")
meters = float(dist)* 1000
print("{}km = {}m".format(dist,meters))

print("This part takes the users name and height (in centimeters), \
     and outputs a summary sentence.")
name = input("Enter a number for a distance: ")
height = input("Enter your height in centimeters: ")
print("{} is {}cms tall".format(name,height))