name_set = set()

name_status = []

while True:
    name = input("Enter a name (or press Enter to finish): ")

    if name == "":
        break

    if name in name_set:
        name_status.append("Existing name")
    else:
        name_status.append("New name")
        name_set.add(name)

for status in name_status:
    print(status)

print("Entered names:")
for name in name_set:
    print(name)

