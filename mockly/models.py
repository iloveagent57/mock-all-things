import time
from datetime import datetime

ABSOLUTE_ZERO_IN_F = -459.67


class Box(object):
    def __init__(self, food):
        self.__food = food
        self.__delivered_at = datetime.max

    @property
    def food(self):
        return self.__food

    @property
    def delivered_at(self):
        return self.__delivered_at

    def deliver(self):
        self.__delivered_at = datetime.utcnow()


class Pizza(object):
    def __init__(self, *args):
        if args:
            self.toppings = [topping for topping in args]
        else:
            self.toppings = []
        self.temperature = 100.0

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, toppings):
        if toppings is None:
            self.__toppings = []
        else:
            self.__toppings = toppings

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temp):
        self.__temperature = float(max(ABSOLUTE_ZERO_IN_F, temp))

    def prepare(self):
        self._cook()
        return Box(self)

    def _cook(self):
        while self.temperature < 500.0:
            time.sleep(0.5)
            self.temperature += 100.0
            print 'Pizza now @ %s degrees F.' % self.temperature


class Topping(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
