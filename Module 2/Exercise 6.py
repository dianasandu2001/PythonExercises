import random

#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6.

first_digit = random.randint(0, 9)
second_digit = random.randint(0, 9)
third_digit = random.randint(0, 9)
print(f"3-digit code where each number is between 0 and 9: {first_digit}{second_digit}{third_digit}")

First_digit = random.randint(1,6)
Second_digit = random.randint(1,6)
Third_digit = random.randint(1,6)
Fourth_digit = random.randint(1,6)
print(f"4-digit code where each number is between 1 and 6: {First_digit}{Second_digit}{Third_digit}{Fourth_digit}")