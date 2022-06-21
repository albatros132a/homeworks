
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):
    default_cargo = 0

    def __init__(self, cargo = 1000, max_cargo = 3000):
        super().__init__(cargo, max_cargo)
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, cargo):
        if (self.cargo + cargo) < self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload(self.cargo)

    def remove_all_cargo(self):
        self.cargo = self.default_cargo
        return self.cargo


def main():
    plane=Plane(1000,3000)

try:
    main()
except CargoOverload as error:
    print(f'Low fuel Error !{error}')
