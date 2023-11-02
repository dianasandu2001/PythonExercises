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

class Race(Car):

    def __init__(self, name, distance, car_num):
        self.name = name
        self.distance = distance
        self.car_num = car_num
        self.car_list = []
        for c in range(0, car_num):
            regestration_number = "ABC-" + str(c)
            max_speed = random.randint(100, 201)
            self.car_list.append(Car(regestration_number, max_speed))

    def hour_passes(self):
         for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            print(f"{car.registration_num:<15} {car.max_speed:<23} {car.current_speed:<20} {car.travelled_distance:<25}")


    def print_status(self):
        print("{:<10} {:<20} {:<25} {:<20}".format("Reg Num", "Max Speed (km/h)", "Current Speed (km/h)", "Distance (km)"))

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True

race = Race("Grand Demolition Derby", 8000, 10)
hour = 0

while not race.race_finished():
    race.hour_passes()
    hour += 1
    print(f"\nHour {hour} of the race:")
    if hour % 10 == 0:
        print(f"\n {hour} hours are passed\n")
        race.print_status()
