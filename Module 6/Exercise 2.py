import random
def dice_roll(side):
    return random.randint(1, side)

max_side = int(input("Enter the number of sides of the dice: "))
dice = 0

while dice != max_side:
    dice = dice_roll(max_side)
    print(dice)
