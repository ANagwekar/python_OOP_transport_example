import vehicles

class Bus(vehicles.Vehicles):
    def __init__(self, no_passenger, no_wheels, movement, manufacturer, baggage_capacity):
        super().__init__(no_passenger, no_wheels, movement)
        self.manufacturer = manufacturer
        self.baggage_capacity = baggage_capacity

    def open_door(self):
        print("*doors open*, \"where to\"........\"that will be $3.50\"")