from example3 import factorial


def function():
    pass

print(type(function))

# lambda args: expression


def foo(a, b):
    return a ** b


f = lambda x, y: x**y if y > 1 else None
# f1 = lambda x, y: for i in range(10): i ** y  Не работает с циклами

# f2 = lambda x: x(a, b)
# print(f2(lambda x, y: x + y))
# print(f(4, 1))
# print(type(f))


# MAP

list_str = ["1", "2", "3"]
list_int = [1, 2, 3]
l = map(int, list_str)
# print(list(l))
#
# print(list(map(lambda x: x**2, list_int)))
# print(list(map(factorial, list_int)))


# FILTER

lst = [i for i in range(10)]
print(lst)
l1 = filter(lambda x: x % 2 != 0, lst)
print(*l1)
