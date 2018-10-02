import random


class Iterator:
    def __init__(self, n):
        self.index = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
            index = self.index
            self.index += 1
            return index
        else:
            raise StopIteration


class RandomIterator:
    def __init__(self, n):
        self.index = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
            self.index += 1
            return random.randint(1, 1000)
        else:
            raise StopIteration

iterator = Iterator(3)
for i in iterator:
    print(i)

for r in RandomIterator(10):
    print(r)