class Point:
    x = 10
    y = 20

    # def __new__(cls, *args, **kwargs):
    #     print("Inside new method")
    #     return super().__new__(cls)

    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    def add_something(self):
        return self.x + self.y

    def foo(self, *args):
        if len(args) == 2:
            return "2"
        elif len(args) == 3:
            return "3"

    def __setattr__(self, key, value):
        if key in ('color', 'shape'):
            self.__dict__[key] = value

    # def __getattribute__(self, item):
    #     if item == "x":
    #         return self.x

    def __getattr__(self, item):
        if item == 'z':
            print("No such attribute")


# def add_something():
#     pass

# print(Point.x)
# print(Point.y)
# print(Point.add_something())

# print(Point.__dict__)

Point.x = 15
print(Point.x)

p1 = Point(color='black', shape='circle')
# print(type(p1) == Point)
p2 = Point(color='red', shape='square')
# print(id(p2))

# print(p2.add_something())
# print(p2.color)
# print(p2.shape)

# p2.color = "blue"
# print(p2.__dict__)
# setattr(p2, 'color', 'blue')
# print(p2.color)

# res = p2.foo(2, 3, 3)
# print(res)


# print(p2.z)
# print(p2.x)

# del Point.x

# del p2.x
# print(p2.__dict__)

# if hasattr(Point, 'x'):
#     delattr(Point, 'x')
#
# print(Point.__dict__)
