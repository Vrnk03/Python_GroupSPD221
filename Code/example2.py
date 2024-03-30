from typing import List, Dict


# Type hints

# def sum_numbers(*args):
#     res = sum(args)
#     return res


# def calculate_area(r: int, pi: float, flag: bool) -> float | int:
#     if flag:
#         res = sum_numbers(r, pi)
#         return res
#     else:
#         return int(pi * pow(r, 2))


# print(calculate_area(2, 3.14, False))


def processed_string(str_: str) -> str:
    l_str = str_.split()
    return l_str[0]


def sum_numbers(nums: List[int]) -> int:
    return sum(nums)


def check_values(dct: Dict[str, int]) -> str:
    pass
