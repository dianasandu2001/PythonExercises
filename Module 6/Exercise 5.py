def remove_odd_numbers(input_list):
    return [x for x in input_list if x % 2 == 0]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_list = remove_odd_numbers(original_list)

num_input = 0
while True:
    num_input = input("Enter a number (Enter to exit): ")
    if num_input == "":
        break
    else:
        original_list.append(float(num_input))

print("Original List:", original_list)
print("Cut-down List:", cut_down_list)
