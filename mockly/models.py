from datetime import datetime
import random
import time


ABSOLUTE_ZERO_IN_F = -459.67


class Order(object):
    def __init__(self, items=None):
        self.__items = items if items else []
        self.__delivered_at = datetime.max

    @property
    def items(self):
        return self.__items

    def add_item(self, item):
        self.__items.append(item)

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

    def quick_order(self):
        self._cook()
        return Order([self])

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


TOPPINGS = {
    'worst': [Topping('Olive'), Topping('Feta')],
    'weak': [Topping('Onion'), Topping('Pepper'), Topping('Mushroom'), Topping('Broccoli')],
    'best': [Topping('Bacon'), Topping('Pepperoni'), Topping('Meatball'), Topping('Sausage'),
             Topping('Ham'), Topping('MOAR CHEESE'), Topping('Anchovy'), Topping('Fried Egg')]
}

def pizza_party(num_pies=3):
    for _ in xrange(num_pies):
        yield construct_pizza()


THRESHOLDS = {
    'worst': 0.95,
    'weak': 0.5,
    'best': 0.05
}

def construct_pizza():
    toppings = []
    num = random.random()
    for key, threshold in THRESHOLDS.iteritems():
        if num >= threshold:
            quantity = int((num - threshold) / 0.10) + 1
            population = TOPPINGS[key]
            toppings.extend(random.sample(population, min(len(population), quantity)))
    return Pizza(*toppings)
