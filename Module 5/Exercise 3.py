num_input = int(input("Enter an integer: "))
prime_check_list = []

for i in range(num_input):
    remainder = num_input % (i+1)
    if remainder == 0:
        prime_check_list.append(i+1)

if len(prime_check_list) > 3:
    print("Your number is not prime.")
else:
    print("Your number is prime.")

