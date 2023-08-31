import math
"""
#Exercise 2.1
user = input("Please enter your name here.")
print(f"Hello {user}!")

#Ecercises 2.2
radius = float(input("Enter a radius of a circle here."))
area = float(math.pi) * math.sqrt(radius)
print(f"The area of your circle is = {area: .3f}")

#Ecercise 2.3
length = float(input("Enter the length of a rectangle"))
width = float(input("Enter the width of a rectangle"))
perimeter = 2*length + 2*width
print(f"The perimeter of your ractangle is {perimeter: .1f}")

#Exercise 2.4
numb1 = int(input("Enter a number"))
numb2 = int(input("Enter another number"))
numb3 = int(input("Enter yet another number"))
sum = numb1 + numb2 + numb3
print(f"The sum of your numbers is {sum}")
product = numb1 * numb2 * numb3
print(f"The product of your numbers is {product}")
average = sum/3
print(f"The average of your numbers is {average}")
"""
#Exercise 2.5
talent_input = float(input("Enter talents here:"))
pound_input = float(input("Enter pounds here:"))
lot_input = float(input("Enter pounds here:"))

lot_variable = 13.3
pound_variable = 32 * lot_variable
talent_variable = 20 * pound_variable

lot_value = lot_variable * lot_input
pound_value = pound_variable * pound_input
talent_value = talent_variable * talent_input

weight_in_g = lot_value + pound_value + talent_value
weight_in_kg = weight_in_g / 1000
grams = weight_in_g % 1000

print(f"The weight you have entered is {int(weight_in_kg)}kg and {int(grams)}g")