import random

def dice_roll ():
    dice = random.randint(1,7)
    return dice

dice = 0

while dice != 6:
    dice = dice_roll()
    print(dice)
