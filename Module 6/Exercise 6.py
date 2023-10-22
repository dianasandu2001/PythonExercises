import math

def calc_unit_price(diameter,price):
    pizza_area = math.pi * (diameter/2)**2
    unit_price = price / (pizza_area/10000)
    return unit_price


print("Pizza 1: ")
diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
price1 = float(input("Enter the price of the first pizza (in euros): "))

unit_price1 = calc_unit_price(diameter1, price1)
print(f"\nUnit price of Pizza 1: {unit_price1:.2} euros per square meter.")

print("\nPizza 2: ")
diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
price2 = float(input("Enter the price of the second pizza (in euros): "))

unit_price2 = calc_unit_price(diameter2, price2)
print(f"\nUnit price of Pizza 2: {unit_price2:.2} euros per square meter.")

if unit_price1 < unit_price2:
    print("\nPizza 1 provides better value for money.")
elif unit_price2 < unit_price1:
    print("\nPizza 2 provides better value for money.")
else:
    print("\nBoth pizzas have the same unit price.")