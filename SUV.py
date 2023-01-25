import cars

class SUV(cars.Car):
    def __init__(self, no_passenger, no_wheels, movement, make, model, top_speed, folding_seats, capacity):
        super().__init__(no_passenger, no_wheels, movement, make, model, top_speed)
        self.folding_seats = folding_seats
        self.capacity = capacity