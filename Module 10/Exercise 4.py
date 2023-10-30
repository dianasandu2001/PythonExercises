#This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the
# following properties: name, distance in kilometers and a list of cars participating in the race. The class has an
# initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding
# properties in the class. The class has the following methods:

    #hour_passes, which performs the operations done once per hour in the original exercise: generates a random change
# of speed for each car and calls their drive method.
    #print_status, which prints out the current information of each car as a clear, formatted table.
    #race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven
# the entire distance of the race.

#Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list
# of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the
# hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current
# status is printed out using the print_status method every ten hours and then once more at the end of the race.

import random

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
