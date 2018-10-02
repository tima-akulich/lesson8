class Singleton(type):
    _object = None

    def __call__(cls, *args, **kwargs):
        if not cls._object:
            cls._object = super().__call__(*args, **kwargs)
        return cls._object


class Cat(metaclass=Singleton):
    pass


class Dog:
    pass

c1 = Cat()
c2 = Cat()
c3 = Cat()
c4 = Cat()
c5 = Cat()

d1 = Dog()
d2 = Dog()

print(c1 is c2, c1 is c3, c1 is c5, c4 is c5)
print(d1 is d2)
