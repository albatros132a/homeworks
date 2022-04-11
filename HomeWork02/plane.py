"""
создайте класс `Plane`, наследник `Vehicle`
в модуле plane создайте класс Plane
класс Plane должен быть наследником Vehicle
добавьте атрибуты cargo и max_cargo классу Plane
добавьте max_cargo в инициализатор (переопределите родительский)
объявите метод load_cargo, который принимает число, проверяет,
что в сумме с текущим cargo не будет перегруза, и обновляет значение,
в ином случае выкидывает исключение exceptions.CargoOverload
объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, которое было до обнуления

"""

class Plane(Vehicle):

    def __init__(self,cargo,max_cargo):
        super().__init__(cargo,max_cargo)
        self.max_cargo=max_cargo
        self.cargo=cargo

    def load_cargo(self,cargo):
        try:
            if (self.cargo+cargo)<self.max_cargo:
                self.cargo+=cargo
        except exceptions.CargoOverload as error:
            print(f'Cargo ever load Error !{error}')

    def remove_all_cargo(self):
        return self.cargo=super().cargo


