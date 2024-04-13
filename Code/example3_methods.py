# @staticmethod and @classmethod


class SomeClass:
    MIN_VALUE = 1
    MAX_VALUE = 20

    def __init__(self, x, y):
        if self.validate_value(x) and self.validate_value(y):
            self.x = x
            self.y = y
        else:
            raise ValueError

    @classmethod
    def validate_value(cls, val):
        return cls.MIN_VALUE <= val <= cls.MAX_VALUE

    def get_params(self):
        return self.x, self.y

    @staticmethod
    def get_area(r, pi=3.14):
        return pi * r ** 2


sc = SomeClass(1, 10)
# params = sc.get_params()
# print(params)

params = SomeClass.get_params(sc)
print(params)

valid = SomeClass.validate_value(21)
print(valid)

print(SomeClass.get_area(5))
print(sc.get_area(5))




