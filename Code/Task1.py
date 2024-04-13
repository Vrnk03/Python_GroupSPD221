"""
Реализовать класс Counter с параметром count и двумя методами increase и reset
"""


class Counter:

    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def reset(self):
        self.count = 0


counter = Counter()
print(counter.count)
counter.increase()
print(counter.count)
counter.increase()
print(counter.count)
counter.reset()
print(counter.count)
