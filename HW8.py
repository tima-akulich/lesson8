def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator is None:
            if isinstance(numerator, int):
                self.num = numerator
                self.den = 1
            elif isinstance(numerator, float):
                str_f = str(numerator)
                c = abs(str_f.find('.') - len(str_f)) - 1
                self.num = int(numerator * 10 ** c)
                self.den = int(10 ** c)
        else:
            self.num = numerator
            self.den = denominator
            
    def __str__(self):
        if self.num > self.den:
            whole = self.num // self.den
            new_num = self.num - (whole * self.den)
            if new_num == 0:
                return str(whole)
            else:
                return str(whole) + " " + str(new_num) + "/" + str(self.den)
        else:
            return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __pow__(self, other):
        new_num = self.num ** other
        new_den = self.den ** other
        _gcd = gcd(new_num, new_den)
        return Fraction(new_num // _gcd, new_den // _gcd)

    def __eq__(self, other):
        num = self.num * other.den
        num2 = other.num * self.den
        return num == num2

    def __lt__(self, other):
        num = self.num * other.den
        num2 = other.num * self.den
        return num < num2

    def __gt__(self, other):
        num = self.num * other.den
        num2 = other.num * self.den
        return num > num2

    def __le__(self, other):
        num = self.num * other.den
        num2 = other.num * self.den
        return num <= num2

    def __ge__(self, other):
        num = self.num * other.den
        num2 = other.num * self.den
        return num >= num2


# f = Fraction(7, 5)
# f1 = Fraction(3, 4)
# f2 = Fraction(3, None)
# f3 = Fraction(3.1, None)
#
# print(f)
# print(f1)
# print(f2)
# print(f3)
# print('Sum: ')
# print(f + f1)
# print('Sub: ')
# print(f - f1)
# print('Mul: ')
# print(f * f1)
# print('Div: ')
# print(f / f1)
# print('Pow: ')
# print(f ** 2)
# print(f1 ** 3)
# print('Eq: ')
# print(f == f1)
# print('Lt: ')
# print(f < f1)
# print('Gt: ')
# print(f > f1)
