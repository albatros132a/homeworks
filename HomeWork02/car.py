

from HomeWork02.base import Vehicle

class Car(Vehicle):
    pass

    def __init__(self, engine):
     #   super().__init__())
        self.engine=engine

    def set_engine(self,engine):
        return self.engine

car=Car(2.0)
car.set_engine(2.0)