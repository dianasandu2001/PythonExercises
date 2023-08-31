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