"""
Реализовать класс Point с параметрами x y и метод dist(), который рассчитывает
евклидово расстояние
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        res = ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
        return res


p1 = Point(1, 3)
p2 = Point(1, 4)
d = p1.dist(p2)

print(d)