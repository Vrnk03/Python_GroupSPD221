"""
Дано натуральное число N, вывести все числа от N до 1 ( и от 1 до N)
Использовать рекурсию.

5
"""


def from_n_to_one(n: int) -> int:
    print(n, end=" ")
    if n == 1:
        return n
    else:
        from_n_to_one(n - 1)


from_n_to_one(5)
print()


def from_one_to_n(n: int, current=1):
    print(current, end=" ")
    if current == n:
        return current
    else:
        return from_one_to_n(n, current=current + 1)

breakpoint()
from_one_to_n(5)
