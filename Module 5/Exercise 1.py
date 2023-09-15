import random

dice_amount = int(input("Enter the number of dice: "))
dice_list = []

for i in range(dice_amount):
    dice_roll = random.randint(1,6)
    dice_list.append(dice_roll)

dice_sum = sum(dice_list)
print(dice_sum)