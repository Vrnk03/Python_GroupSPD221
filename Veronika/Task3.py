def func(lst: list) -> list:
    l = list(dict.fromkeys(lst))
    return l
l = [1, 15, 35, 4, 1, 15]
print(func(l))
