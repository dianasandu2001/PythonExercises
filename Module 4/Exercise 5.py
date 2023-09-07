username = str("python")
password = str("rules")
counter = 0

username_input = str(input("Enter username: "))
password_input = str(input("Enter password: "))

while username != username_input or password != password_input or counter < 5:
    counter += 1
    if counter == 5:
        print("Access denied!")
        break
    elif username == username_input and password == password_input:
        print("Welcome!")
        break
    else:
        print("Username or Password incorrect, try again.")
        username_input = input("Enter username: ")
        password_input = input("Enter password: ")
