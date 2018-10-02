class MyMeta(type):
    def __new__(cls, class_name, parents, attr):
        new_attr = {}
        for key, value in attr.items():
            new_attr[key.upper()] = value
            new_attr[key] = value
        return type.__new__(cls, class_name, parents, new_attr)


Class = MyMeta('Class', tuple(), {'a': 1})
c = Class()
print(c.a, c.A)


class Class1(metaclass=MyMeta):
    a = 1
    b = 2

    def foo(self):
        pass

c = Class1()
print(dir(c))

