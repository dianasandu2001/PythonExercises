def sum_of_nums(nums):
    total = 0
    for num in nums:
        total += num
    return total

num_list = []

num_input = 0
while True:
    num_input = input("Enter a number (Enter to exit): ")
    if num_input == "":
        break
    else:
        num_list.append(float(num_input))

sum = sum_of_nums(num_list)
print(sum)
