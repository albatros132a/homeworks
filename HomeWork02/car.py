

from base import Vehicle

from HomeWork02.engine import Engine

class Car(Vehicle):
    pass

    def __init__(self, engine):
        self.engine=engine

    def set_engine(self,engine):
        return self.engine

car=Car()
car.set_engine()