
class FracNum:

    def __init__(self, value):
        self.value = value

    def frac_manner(self):
        raise NotImplementedError

    def _get_value(self, other):
        value = other
        if isinstance(other, FracNum):
            value = input()
        return value

    def __lt__(self, other):
        return self._get_value() < self._get_value(other)

    def __add__(self, other):
        pass
    __iadd__ = __add__

    def __gt__(self, other):
        return self._get_value() > self._get_value(other)

    def _get_parts(self):
        intpart = int(abs(self.value))
        numer = str(round(abs(self.value) - intpart, 5))
        denom = 10 ** (len(numer) - 2)
        try:
            numer = int(numer[2:])
        except ValueError:
            numer = int(numer)
        return self.value, intpart, numer, denom

    def output(self, _get_parts):
        parts = _get_parts

        def _sign_of_output():
            if parts[0] < 0:
                return '-(%s)' % result
            elif parts[0] > 0:
                return result

        def _reduct(numer, denom):
            while True:
                if numer % 5 == 0 and denom % 5 == 0:
                    numer /= 5
                    denom /= 5
                elif numer % 2 == 0 and denom % 2 == 0:
                    numer /= 2
                    denom /= 2
                else:
                    return int(numer), int(denom)

        if parts[0] == 0:
            return '0'
        elif parts[0] % 1 == 0:
            return parts[0]
        elif parts[1] == 0:
            result = '%s/%s' % (_reduct(parts[2], parts[3]))
        elif parts[2] == '0':
            result = '%s' % (parts[1])
        else:
            res = _reduct(parts[2], parts[3])
            result = '%s + %s/%s' % (parts[1], res[0], res[1])
        return _sign_of_output()


if __name__ == '__main__':

    a = FracNum(123.123)
    print(a.output(a._get_parts()))






