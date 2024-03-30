# def count_down(n: int) -> int:
#     if n == 1:
#         return n
#     else:
#         print(n)
#         return count_down(n - 1)
#
#
# print(count_down(10))


def get_GCD(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return get_GCD(b, a % b)


# print(get_GCD(35, 15))


def get_sum(n: int) -> int:
    if n <= 1:
        return n
    else:
        return n + get_sum(n - 1)


# print(get_sum(5))

def factorial(num: int) -> int:
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(4))

