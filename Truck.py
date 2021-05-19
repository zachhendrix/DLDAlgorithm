# Truck object class which contains getters and setters as well as an 'add_mileage' method which adds mileage traveled
# and a 'remove_cargo' method which removes the package ID specified.

class Truck:
    mileage = 0
    miles_per_min = .3
    location = "At Hub"
    cargo = []
    cargo_list = cargo

    def __init__(self, _mileage, _miles_per_min, _location, _cargo):
        self.mileage = _mileage
        self.miles_per_min = _miles_per_min
        self.location = _location
        self.cargo = _cargo

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, x):
        self.mileage = 0

    def add_mileage(self, x):
        self.mileage = self.mileage + x

    def get_miles_per_min(self):
        return self.miles_per_min

    def get_location(self):
        return self.location

    def set_location(self, x):
        self.location = x

    def get_cargo(self):
        return self.cargo

    def set_cargo(self,x):
        self.cargo = x

    def remove_cargo(self, x):
        self.cargo.remove(x)