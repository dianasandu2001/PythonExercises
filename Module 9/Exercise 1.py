class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distanc = 0

    def print_info(self):
        print(f"Registration number:{self.registration_num}\nMaximum speed:{self.max_speed}")

car1 = Car("ABC-123", 142)
car1.print_info()
