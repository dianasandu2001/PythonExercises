import random

print("The computer will generate a number between 1 and 10, try to guess it.")
correct_numb = random.randint(1,10)
guess_numb = int(input("Guess number: "))
while correct_numb != guess_numb:
    if correct_numb < guess_numb:
        print("Too high")
        guess_numb = int(input("Try again: "))
    else:
        print("Too small")
        guess_numb = int(input("Try again: "))
print("You have guessed the right number!")