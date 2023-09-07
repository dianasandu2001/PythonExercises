num = input("Enter a number: ")
smallest_num = num
largest_num = num

while num != "":
    if num < smallest_num:
        smallest_num = num
    elif num > largest_num:
        largest_num = num
    num = input("Enter a number: ")

print(f"{smallest_num} is the smallest number and {largest_num} is the largest number of the numbers entered.")
