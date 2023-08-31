gender = input("Please enter your biological gender (female or male) here: ")
hemoglobin = float(input("Please enter your hemoglobin level (in g/l)"))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin level is low.")
    elif hemoglobin >= 117 and hemoglobin <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is low.")
    elif hemoglobin >= 234 and hemoglobin <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid gender.")