num_list = []
num_input = input("Enter a number, or press enter to quit: ")

while num_input != "":
    num_list.append(num_input)
    num_input = input("Enter another number, or press enter to quit: ")

#the reverse function works but only for numbers under 10, it treats 12 like a 1 and 35 like a 3 and so on.
num_list.sort(reverse=True)

for i in range(5):
    print(num_list[i])

