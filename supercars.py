import cars

class Supercars(cars.Car):
    def __init__(self, no_passenger, no_wheels, movement, make, model, fuel, functions, top_speed):
        super().__init__(no_passenger, no_wheels, movement, make, model, fuel)
        self.functions = functions
        self.top_speed = top_speed

    def drive_supercar(self):
        print(f"{self.make} {self.model} goes vroom vroom *obnoxiously loud*")