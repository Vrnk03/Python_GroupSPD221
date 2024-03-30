"""
Написать функцию, которая принимает посдедовательность слов (через запятую)
и выводит только уникальные слова, отсортированные в алфавитном порядке

red, black, white, red, green, blue, black
black, blue, green, red, white
"""

lst = ["red", "black", "white", "red", "green", "blue", "black"]


def make_unique(*args):
    tmp = sorted(list(set(*args)))
    return tmp


# print(make_unique(lst))


def make_unique_v2(lst_: list) -> list:
    tmp = sorted(lst_)
    p1, p2 = 0, 0

    while p1 < len(tmp):
        while p2 < len(tmp) - 1 and tmp[p2] == tmp[p2 + 1]:
            p2 += 1

        p1 += 1
        p2 += 1
        if p2 == len(tmp):
            return tmp[:p1]
        tmp[p1] = tmp[p2]

    return tmp[:p1]


print(make_unique_v2(lst))

