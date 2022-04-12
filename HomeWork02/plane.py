
from HomeWork02.exceptions import CargoOverload
from HomeWork02.base import Vehicle

def main():

    class Plane(Vehicle):
        default_cargo = 1000
        cargo=1000
        max_cargo=3000

        def __init__(self, cargo, max_cargo):
            super().__init__(cargo, max_cargo)
            self.max_cargo = max_cargo
            self.cargo = cargo

        def load_cargo(self,cargo):
            try:
                if (self.cargo + cargo) < self.max_cargo:
                    self.cargo += cargo
            except CargoOverload as error:
                print(f'Cargo ever load Error !{error}')

        def remove_all_cargo(self):
            self.cargo = self.default_cargo

try:
    main()
except CargoOverload as error:
    print(f'Low fuel Error !{error}')
