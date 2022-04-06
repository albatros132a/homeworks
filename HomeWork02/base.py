from abc import ABC


class Vehicle(ABC):
    pass


from abc import ABC

from HomeWork_02.exceptions import exceptions



class Vehicle(ABC):
  ''''  weight=2500
    started=True
    fuel=100%
    fuel_consumption=9.5
    distance
   '''
    pass

    def __init__(self,weight, fuel, fuel_consumption)
        self.weigh=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption

    def start(self):
        if self.started==True:
            return self.started
        else check_fuel

'''
try:
self.started==True
else:


'''


    def check_fuel(self):
            if fuel > 0:
                return True
            else raise exceptions.LowFuelError()

    def move(self,fuel):
        self.fuel
        move_fuel=distance/100*fuel_consumption
        if (self.fuel-move_fuel)>0:
            return self.fuel=self.fuel-move_fuel
        else:
            raise exceptions.NotEnoughFuel()

car_1=Vehicle(2500,100,9.5)