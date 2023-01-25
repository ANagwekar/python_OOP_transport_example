class Vehicles:
    def __init__(self, no_passenger, no_wheels, movement):  #defines attributes of the class (properties)
        self.no_passenger = no_passenger
        self.no_wheels = no_wheels
        self.movement = movement
        self.__seats = 'yes'

    def set_seats(self, seating_available): #setter function    #additional functions define
        self.__seats = seating_available

    def get_seats(self): #getter method
        return self.__seats
