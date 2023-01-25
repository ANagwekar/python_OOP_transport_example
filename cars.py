import vehicles

class Car(vehicles.Vehicles):   #defines attributes of the class (properties)#
    def __init__(self, no_passenger, no_wheels, movement, make, model, fuel):
        super().__init__(no_passenger, no_wheels,movement)
        self.make = make
        self.model = model
        self.fuel = fuel


    def drive(self): #additional functions define
        print("\"vroom vroom\" playing tokyo drift")

    def horn(self):
        print("honk honk!")

