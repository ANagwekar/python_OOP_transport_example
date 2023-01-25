import supercars
import vehicles
import bus

busses = vehicles.Vehicles(48,4,'road')
busses.set_seats('yes') #set the hidden attribute
print(busses.no_wheels)
print(busses.no_passenger)
print(busses.get_seats()) #get the hidden attribute

B10M = bus.Bus(48,4,'road','Volvo',5720)
print(B10M.no_passenger)
print(B10M.no_wheels)
print(B10M.manufacturer)

LaFerrari = supercars.Supercars(2,4,'road','Ferrari','LaFerrai','Diesel','4 wheel drive', 218)
LaFerrari.drive_supercar()
LaFerrari.drive()

