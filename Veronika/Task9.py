
from typing import List

def foo(nums: List[int]) -> List[int]:
    total = 1
    for num in nums:
        total *= num
    result = [total // num for num in nums]
    return result

print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))
