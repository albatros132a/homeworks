from homework_02.exceptions import LowFuelError, NotEnoughFuel

from abc import ABC


class Vehicle(ABC):
    started = False

    def __init__(self, weight=2500, fuel=70, fuel_consumption=9.5):
        self.weigh = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started != True:
            if check_fuel():
                self.started= True


    def check_fuel(self):

        if self.fuel > 0:
            return True
        else:
            raise LowFuelError(self.fuel)

    def move(self):

        move_fuel = self.distance * self.fuel_consumption
        if (self.fuel - move_fuel) > 0:
            self.fuel = (self.fuel - move_fuel)

        else:
            raise NotEnoughFuel(self.fuel)


def main():
    car_1 = Vehicle(2500, 100, 9.5)
    distance = 70

try:
    main()
except LowFuelError() as e:
    print(f'Low fuel Error !{e}')
except NotEnoughFuel() as e:
    print(f'Not enough fuel Error !{e}')
