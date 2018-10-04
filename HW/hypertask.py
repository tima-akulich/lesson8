def _gcd(i, j):
    while i % j != 0:
        ii = i
        jj = j
        i = jj
        j = ii % jj
    return j


class fraction:
    def __init__(self, *args):
        if len(args) == 2 and type(args[0]) is int and type(args[1]) is int and args[1] >= 0:
            reduc = _gcd(args[1], 10 ** len(str(args[1])))
            self.denominator = 10 ** len(str(args[1])) / reduc
            self.numerator = args[1] / reduc + args[0] * self.denominator
        elif len(args) == 1 and type(args[0]) is float:
            self.denominator = 10 ** (len(str(args[0])[str(args[0]).find('.') + 1:]))
            self.numerator = int(str(args[0])[str(args[0]).find('.') + 1:])
            reduc = _gcd(self.numerator, self.denominator)
            self.numerator /= reduc
            self.denominator /= reduc
            self.numerator += int(str(args[0])[:str(args[0]).find('.')]) * self.denominator
        else:
            raise ValueError

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return fraction(n / d)

    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return fraction(n / d)

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return fraction(n / d)

    def __truediv__(self, other):
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return fraction(n / d)

    def __pow__(self, a):
        n = self.numerator ** a
        d = self.denominator ** a
        return fraction(n / d)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __str__(self):
        if self.numerator > self.denominator:
            _int_p = int(self.numerator // self.denominator)
            new_num = int(self.numerator - self.denominator * _int_p)
            return str(_int_p) + ' ' + str(new_num) + '/' + str(int(self.denominator))
        elif self.numerator == self.denominator:
            return '1'
        elif self.numerator < self.denominator:
            return str(int(self.numerator)) + '/' + str(int(self.denominator))
