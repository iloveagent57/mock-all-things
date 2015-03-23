class Foo(object):
    def __init__(self, x):
        self._x = x

    def add(self, y):
        self.__x += y