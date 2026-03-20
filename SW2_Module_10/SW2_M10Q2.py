class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def go_to_floor(self,floor):
        self.current_floor = floor
        print(f"Hissi on kerroksessa {self.current_floor}")
    def floor_up(self):
        self.current_floor += 1
        print(f"Hissi on kerroksessa {self.current_floor}")

    def floor_down(self):
        self.current_floor += (-1)
        print(f"Hissi on kerroksessa {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, elevator_amount):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators_count = elevator_amount
        self.elevators = [
            Elevator(self.bottom_floor,self.top_floor)
            for i in range(elevator_amount)
            ]
    def run_elevator(self,index,floor):
        self.elevators[index].go_to_floor(floor)

pissgunk = Building(0,10,5)
print(pissgunk.elevator)
#pissgunk.run_elevators()
#print(elevator)

