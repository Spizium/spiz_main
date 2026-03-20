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