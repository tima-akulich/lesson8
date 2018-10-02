import math


class Figure:
    def square(self):
        raise NotImplementedError

    def _get_value(self, other):
        value = other
        if isinstance(other, Figure):
            value = other.square()
        return value

    def __lt__(self, other):
        return self.square() < self._get_value(other)

    def __add__(self, other):
        pass
    __iadd__ = __add__

    def __gt__(self, other):
        return self.square() > self._get_value(other)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        return self.a * self.b * self.c


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def square(self):
        return self.r ** 2 * math.pi


if __name__ == '__main__':
    c = Circle(5)
    t = Triangle(1, 2, 3)
    print(c < t)
