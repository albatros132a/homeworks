

from base import Vehicle

from engine import Engine

class Car(Vehicle):
    pass

    def __init__(self, engine):
        self.engine=engine

    def set_engine(self):
        car=Car()+Engine()

"""
объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car

"""