

from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    def __init__(self, engine):
        self.engine=engine

    def set_engine(self,engine):
        engine = Engine(2.0,4)
        car = Car(engine)
        return car
