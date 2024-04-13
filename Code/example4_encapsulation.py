class A:

    def __init__(self, a, b):
        self._a = a
        self.__b = b

    @property
    def a(self):
        return self._a

    def get_b(self):
        return self.__b

    def set_b(self, val):
        self.__b = val


# a - public attr
# _a - protected attr
# __a - private attr


a = A(1, 2)
a._a = 3
print(a.a)
print(a.__b)


# class B(A):
#
#     def __init__(self, a, b):
#         super(B, self).__init__(a, b)
#         self.b = b
#