# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    '''
        Base Class(Parent Class)
    '''
    pass


class FlightVehicle(Vehicle):
    '''
        Base Class(Parent Class)
    '''
    pass


class Starship(FlightVehicle):
    '''
        Base Class(Parent Class)
    '''
    pass


class GroundVehicle(Vehicle):
    '''
        Child Class (Inherits Attributes and Mothods from Vehicle)
    '''
    pass


class Car(GroundVehicle):
    '''
        Child Class of GroundVehicle (Inherits Attributes and Mothods from GroundVehicle)
    '''
    pass


class Motorcycle(GroundVehicle):
    '''
        Child Class of GroundVehicle (Inherits Attributes and Mothods from GroundVehicle)
    '''
    pass

# Flight Vehicle


class Airplane(FlightVehicle):
    '''
        Child Class (Inherits Attributes and Mothods from FlightVehicle)
    '''
    pass
