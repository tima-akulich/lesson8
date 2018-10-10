class FloatNumber():
    def __init__(self, number, decimal_places):
        if not isinstance(number, int) or not isinstance(decimal_places, int):
            raise TypeError('Not integer')
        elif decimal_places < 0:
            raise TypeError("Decimal places must be 0 or more")
        else:
            self.number = number
            self.divider = decimal_places


class Float(FloatNumber):
    def float_num(self):
        return int(self.number) / 10 ** int(self.divider)

    def __eq__(self, other):
        return self.float_num() == other.float_num()

    def __ne__(self, other):
        return self.float_num() != other.float_num()

    def __lt__(self, other):
        return self.float_num() < other.float_num()

    def __gt__(self, other):
        return self.float_num() > other.float_num()

    def __le__(self, other):
        return self.float_num() <= other.float_num()

    def __ge__(self, other):
        return self.float_num() >= other.float_num()

    def __add__(self, other):
        return self.float_num() + other.float_num()

    def __radd__(self, other):
        return other.float_num() + self.float_num()

    def __sub__(self, other):
        return self.float_num() - other.float_num()

    def __rsub__(self, other):
        return other.float_num() - self.float_num()

    def __mul__(self, other):
        return self.float_num() * other.float_num()

    def __rmul__(self, other):
        return other.float_num() * self.float_num()

    def __floordiv__(self, other):
        return self.float_num() // other.float_num()

    def __rfloordiv__(self, other):
        return other.float_num() // self.float_num()

    def __div__(self, other):
        return self.float_num() / other.float_num()

    def __rdiv__(self, other):
        return other.float_num() / self.float_num()

    def __mod__(self, other):
        return self.float_num() % other.float_num()

    def __rmod__(self, other):
        return other.float_num() % self.float_num()

    def __pow__(self, other):
        return self.float_num() ** other.float_num()

    def __rpow__(self, other):
        return other.float_num() ** self.float_num()

    def __round__(self, other):
        return round(self.float_num(), int(other))
