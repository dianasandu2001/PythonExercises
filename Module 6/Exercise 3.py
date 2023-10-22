def gallon_to_liter(gallon):
    liter = gallon*3.78541
    return liter

while True:
    V_gallon = float(input("Enter a volume of gallons: "))
    if V_gallon >= 0:
        print(f"Your volume equals {gallon_to_liter(V_gallon)} l")
    else:
        break
