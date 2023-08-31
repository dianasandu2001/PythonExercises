zander_length = float(input("Enter the length of a zander here: "))

if zander_length <= 42:
    print("Please release the fish back into the lake")
    zander_length_input = 42 - zander_length
    print(f"The zander is {zander_length_input}cm short of the length requirement")
else:
    print(f"Congratulations on your new {int(zander_length)}cm zander fish!")