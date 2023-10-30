# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are
# created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following
# operations are performed:
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accerelate method.
# Each car is made to drive for one hour. This is done with the drive method.
import random


# The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car
# are printed out formatted into a clear table.
class Car:
    def __init__(self, registration_num, max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def print_info(self):
        print(f"Registration number:{self.registration_num}\nMaximum speed:{self.max_speed}")

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed < 0 or self.current_speed > self.max_speed:
            if self.current_speed < 0:
                self.current_speed = 0
            elif self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
        else:
            pass
        return self.current_speed

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed
        return self.travelled_distance

    def print_table(self):
        print("{:<10} {:<15} {:<15} {:<15}".format("Reg Num", "Max Speed (km/h)", "Current Speed (km/h)", "Distance (km)"))
        print("{:<10} {:<15} {:<15} {:<15}".format(car.registration_num, car.max_speed, car.current_speed, car.travelled_distance))


car_list = []

for i in range(1, 11):
    regestration_number = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car_list.append(Car(regestration_number, max_speed))

hour = 0
race_distance = 10000

while all(car.travelled_distance < race_distance for car in car_list):
    print("")
    print(f"Hour {hour} of the race:")
    print("{:<10} {:<20} {:<25} {:<20}".format("Reg Num", "Max Speed (km/h)", "Current Speed (km/h)", "Distance (km)"))
    for car in car_list:
        car.accelerate(random.randint(-10, 15))
        car.drive(hour)
        print(f"{car.registration_num:<15} {car.max_speed:<23} {car.current_speed:<20} {car.travelled_distance:<25}")
    hour += 1
