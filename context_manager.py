import time


class Timer:
    def __init__(self):
        self.start = time.time()
        self.end = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()

    def current_time(self):
        return (self.end or time.time()) - self.start


with Timer() as timer:
    print(timer.current_time())
    time.sleep(5)
    print(timer.current_time())
a = 1
print(timer.current_time())



