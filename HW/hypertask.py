import re


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
        elif len(args) == 1 and type(args[0]) is str and re.match(r'\d+.\d*[(]\d+[)]', args[0]):
            i1 = args[0][args[0].find('.') + 1: args[0].find('(')] + args[0][args[0].find('(') + 1: args[0].find(')')]
            i2 = args[0][args[0].find('.') + 1: args[0].find('(')]
            if len(i2) == 0:
                i2 = '0'
                i3 = '9' * len(args[0][args[0].find('(') + 1: args[0].find(')')])
            else:
                i3 = '9' * len(args[0][args[0].find('(') + 1: args[0].find(')')]) * 10 ** len(i2)
            i4 = args[0][:args[0].find('.')]
            reduc = _gcd(int(i1) - int(i2), int(i3))
            self.denominator = int(i3) / reduc
            self.numerator = (int(i1) - int(i2)) / reduc + int(i4) * self.denominator
        else:
            raise ValueError

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return fractionn(n, d)

    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return fractionn(n, d)

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return fractionn(n, d)

    def __truediv__(self, other):
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return fractionn(n, d)

    def __pow__(self, a):
        n = self.numerator ** a
        d = self.denominator ** a
        return fractionn(n, d)

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


class fractionn(fraction):
    def __init__(self, n, d):
        self.numerator = n / _gcd(n, d)
        self.denominator = d / _gcd(n, d)
