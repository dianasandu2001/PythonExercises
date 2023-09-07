while True:
    inch_input = float(input("Enter inches to convert to cm: "))
    if inch_input < 0:
        break
    else:
        cm_output = inch_input * 2.54
        print(f"{inch_input} inch = {cm_output} cm")