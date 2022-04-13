from HomeWork02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload

from abc import ABC


class Vehicle(ABC):
    weight = 2500
    started = True
    fuel = 70
    fuel_consumption = 9.5
    distance = 55

    def __init__(self, weight, fuel, fuel_consumption):
        self.weigh = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):

        if self.started == True:
            return self.started
        else:
            return check_fuel

    def check_fuel(self):

        if self.fuel > 0:
            return True
        else:
            raise LowFuelError(self.fuel)

    def move(self):

        move_fuel = self.distance / 100 * fuel_consumption
        if (self.fuel - move_fuel) > 0:
            self.fuel = (self.fuel - move_fuel)

        else:
            raise NotEnoughFuel(self.fuel)


def main():
    car_1 = Vehicle(2500, 100, 9.5)

try:
    main()
except LowFuelError as e:
    print(f'Low fuel Error !{e}')
except NotEnoughFuel as e:
    print(f'Not enough fuel Error !{e}')
