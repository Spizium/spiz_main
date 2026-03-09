class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 2000
        self.car = 0

    def accelerate(self, accelerate):
        car.current_speed = car.current_speed + accelerate

    def drive(self,time):
        car.travelled_distance += car.current_speed * time

car = Car("ABC-123", 142)
print(f"Initial distance: {car.travelled_distance} km")
car.current_speed = 60
car.drive(1.5)
print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")
