class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distanc = 0

    def print_info(self):
        print(f"Registration number:{self.registration_num}\nMaximum speed:{self.max_speed}")

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed < 0 or self.current_speed > self.max_speed:
            print("Invalid change of speed")
            if self.current_speed < 0:
                self.current_speed = 0
            elif self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
        else:
            pass
        print(f"The car's current's speed is now {self.current_speed}")
        return self.current_speed


car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)