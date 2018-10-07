class Fraction:

    def __simply(self,n,d,sign):
        a = abs(n)
        b = abs(d)
        while a % b != 0:
            temp_a = a
            temp_b = b
            a = temp_a
            b = temp_a % temp_b

        ret_n = sign * abs(n) // b
        ret_d = abs(d) // b
        return (ret_n, ret_d)
    def getNumerator(self):
        return  self._nume
    def getDenominator(self):
        return self._deno

    def __init__(self, nume, deno):
        if not isinstance(nume, int):
            raise TypeError('The numerator of fraction must be an integer')
        if not isinstance(deno, int):
            raise TypeError('The denominator of fraction must be an integer')

        if deno == 0:
            raise ZeroDivisionError('division by zero is not defined.')

        if nume == 0:
            self._nume = 0
            self._deno = 1
        else:
            if (nume < 0 and  deno > 0) or (nume > 0 and deno < 0):
                sign = -1
            else:
                sign = 1
            (self._nume, self._deno) = self.__simply(nume, deno, sign)

    def __repr__(self):
        return "" + str(self._nume) + '/' + str(self._deno)

    def __eq__(self,rhs):
        lhs=self
        return(lhs.getNumerator()==rhs.getNumerator()) and (lhs.getDenominator()==rhs.getDenominator())
    def __ne__(self, rhs):
        lhs=self
        return not lhs==rhs
    def __lt__(self, rhs):
        lhs=self
        return lhs.getNumerator()*rhs.getDenominator() < lhs.getDenominator()*rhs.getNumerator()

    def __le__(self, rhs):
         lhs=self
         return not rhs < lhs

    def __gt__(self, rhs):
        lhs=self
        return rhs <lhs

    def __ge__(self, rhs):
        lhs=self
        return not rhs >lhs

    def __add__(self, rhs):
        lhs=self
        nume=lhs.getNumerator()*rhs.getDenominator() +rhs.getNumerator()*lhs.getDenominator()
        deno=lhs.getDenominator()*rhs.getDenominator()
        return Fraction(nume,deno)


    def __sub__(self, rhs):
        lhs=self
        nume=lhs.getNumerator()*rhs.getDenominator() -rhs.getNumerator()*lhs.getDenominator()
        deno=lhs.getDenominator()*rhs.getDenominator()
        return Fraction(nume,deno)

    def __mul__(self, rhs):
        lhs=self
        nume = lhs.getNumerator() * rhs.getNumerator()
        deno = lhs.getDenominator() * rhs.getDenominator()
        return Fraction(nume,deno)

    def __truediv__(self, rhs):
        lhs = self
        nume = lhs.getNumerator() * rhs.getDenominator()
        deno = lhs.getDenominator() * rhs.getNumerator()
        return Fraction(nume, deno)