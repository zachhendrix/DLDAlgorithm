class Truck:
    mileage = 0
    miles_per_min = .3
    cargo = {}

    def __init__(self, mlg, mpm, carg):
        self.mileage = mlg
        self.miles_per_min = mpm
        self.cargo = carg

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))