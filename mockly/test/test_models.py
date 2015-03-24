from datetime import datetime
import unittest

import mock

from .common import MockDateTime

from mockly.models import Box, Pizza, Topping, ABSOLUTE_ZERO_IN_F

class TestBox(unittest.TestCase):
    def test_initialize(self):
        # setup
        food = mock.Mock() # we don't care what the food is, just want a reference to some object

        # method under test
        box = Box(food)

        # assertions
        # for assertEqual, the call convention is to pass in the expected value, then the actual value
        # (and then any message to be printed on failure)
        self.assertEqual(food, box.food, msg='It puts the food in the basket.')
        self.assertEqual(datetime.max, box.delivered_at, msg='It does this whenever it\'s told.')

    def test_food_getter(self):
        food = mock.Mock()

        self.assertEqual(food, Box(food).food)

    def test_delivered_at_getter(self):
        # we don't even care about storing a reference to food here
        self.assertEqual(datetime.max, Box(mock.Mock()).delivered_at)

    def test_deliver(self):
        # we replace the models.datetime class with our own MockDateTime class
        with mock.patch('mockly.models.datetime', MockDateTime):
            food = mock.Mock()
            box = Box(food)

            box.deliver()

            self.assertEqual(MockDateTime.NOW, box.delivered_at)


class TestPizza(unittest.TestCase):
    def test_initialize(self):
        topping_1 = mock.Mock()
        topping_2 = mock.Mock()

        pizza = Pizza(topping_1, topping_2)

        self.assertEqual([topping_1, topping_2], pizza.toppings)
        self.assertAlmostEqual(100.000001, pizza.temperature, places=5, msg='Close enough')

    def test_get_set_toppings(self):
        pizza = Pizza()
        onions, sausage, anchovies = [mock.Mock() for _ in xrange(3)]
        
        self.assertEqual([], pizza.toppings)

        pizza.toppings = [onions, sausage]
        self.assertEqual([onions, sausage], pizza.toppings)

        pizza.toppings.append(anchovies)
        self.assertEqual([onions, sausage, anchovies], pizza.toppings)

        pizza.toppings = None
        self.assertEqual([], pizza.toppings)

    def test_get_set_temperature(self):
        pizza = Pizza()
        pizza.temperature = int(200)

        self.assertAlmostEqual(200.0, pizza.temperature)

        pizza.temperature = -2000.0
        self.assertAlmostEqual(ABSOLUTE_ZERO_IN_F, pizza.temperature)

    def test_prepare(self):
        """
        We wrote some module code, we can use mock here to "wave away" that module,
        letting tests for that specific module run in other test functions.  We can focus
        on only the level of the prepare() method here, particularly on the order of operations,
        adhering to the contract of other function calls.
        """
        with mock.patch('mockly.models.Box.__new__') as box_ctor:
            pizza = Pizza()
            pizza._cook = mock.Mock() # wave our hands about the _cook function

            result = pizza.prepare()

            # First, we assert that _cook is called on our pizza object.
            pizza._cook.assert_called_once_with()
            # Next, we assert that a new Box object is created, initialized with the pizza object
            # __new__ is called with the class as the first argument, then the arguments to __init__
            box_ctor.assert_called_once_with(Box, pizza)
            # Last, assert that the thing returned by prepare() is the result of Box.__new__
            self.assertEqual(box_ctor.return_value, result)

    def test_cook(self):
        """
        We don't want to actually wait for sleep (or another long function) to run, let's mock it out.
        """
        with mock.patch('mockly.models.time.sleep') as sleep:
            pizza = Pizza()

            pizza._cook()

            # sleep should have been called 4 times - 4 passes of loop to go from 100 to 500 in
            # 100 degree increments
            sleep.assert_has_calls([
                mock.call(0.5),
                mock.call(0.5),
                mock.call(0.5),
                mock.call(0.5)
            ])
            # the pizza should be cooked now
            self.assertAlmostEqual(500.0, pizza.temperature)


class TestTopping(unittest.TestCase):
    def test_initialize(self):
        topping = Topping('Pepperoni')
        self.assertEqual('Pepperoni', topping.name)

    def test_getter_setter(self):
        topping = Topping('Pepperoni')
        self.assertEqual('Pepperoni', topping.name)

        topping.name = 'Fried Egg'
        self.assertEqual('Fried Egg', topping.name)