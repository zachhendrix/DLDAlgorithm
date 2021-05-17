# Truck object class which contains getters and setters as well as an 'add_mileage' method which adds mileage traveled
# and a 'remove_cargo' method which removes the package ID specified.
import math


class Clock:
    minutes = 8
    hours = 00
    is_morning = True

    def __init__(self, _hours, _minutes, _is_morning):
        self.hours = _hours
        self.minutes = _minutes
        self.is_morning = _is_morning

    def get_time(self):
        if self.is_morning is True:
            return format(self.hours, '02'), ":", format(self.minutes, '02'), "AM"
        if self.is_morning is not True:
            return format(self.hours, '02'), ":", format(self.minutes, '02'), "PM"

    def set_time(self, x, y, z):
        self.hours = x
        self.minutes = y
        self.is_morning = z

    def add_minute(self, x):
        self.minutes = self.minutes + math.ceil(x)
        while self.minutes >= 60:
            minutes_ref = self.minutes
            self.minutes = minutes_ref - 60
            self.add_hour(1)

    def add_hour(self, x):
        self.hours = self.hours + x
        if self.hours > 11:
            self.is_morning = False
        if self.hours > 12:
            self.hours = 1
