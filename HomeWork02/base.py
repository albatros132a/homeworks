'''

доработайте базовый класс base.Vehicle:
добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
добавьте инициализатор для установки weight, fuel, fuel_consumption
добавьте метод start, который, если ещё не состояние started, проверяет, что топлива больше нуля,
 и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError
добавьте метод move, который проверяет, что достаточно топлива для преодоления переданной дистанции,
и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel
'''

from abc import ABC

from HomeWork_02.exceptions import exceptions

class Vehicle(ABC):
    weight=2500
    started=True
    fuel=100
    fuel_consumption=9.5
    distance=55

    pass

    def __init__(self,weight, fuel, fuel_consumption):
        self.weigh=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption

   # @property
    #def move(self):
     #   return fuel=self.fuel



    def start(self):
        if self.started==True:
            return self.started
        else:
            return check_fuel()



    def check_fuel(self):
        if self.fuel > 0:
            return True
        else:
            raise exceptions.LowFuelError()

    @property
    def move(self,fuel):
        move_fuel=distance/100*fuel_consumption
        if (self.fuel-move_fuel)>0:
            return self.fuel=(self.fuel-move_fuel)
        else:
            raise exceptions.NotEnoughFuel()

car_1=Vehicle()