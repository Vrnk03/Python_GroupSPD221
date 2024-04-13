class A:
    __slots__ = ['p1', 'p2', 'a', 'd']

    # p1 = "test"
    # p2 = 30
    def __init__(self, a):
        self.a = a


print(A.__dict__)
print(A.__slots__[0])
print(A.__slots__)

A.c = "1234"
print(A.__dict__)

a_ = A(1)
print(a_.a)
# print(a_.c)
a_.d = "123"
print(a_.d)

# print(a_.__dict__)
print(a_.__slots__)