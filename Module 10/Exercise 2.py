class Elevator:
    current_floor = 0
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1
    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()
            print(self.current_floor)
        return self.current_floor

class Building:
    elevator_list = []
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators
        for h in range(0, num_elevators):
            h = Elevator(self.bottom_floor, self.top_floor)
            self.elevator_list.append(h)

    def run_elevator(self, index, floor_destination):
        self.elevator_list[index].go_to_floor(floor_destination)


building1 = Building(0, 10, 4)
building1.run_elevator(2, 5)