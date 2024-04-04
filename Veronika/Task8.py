
from typing import List, Tuple

def get_pairs(lst: List) -> List[Tuple]:
    if len(lst) < 2:
        return None
    pairs = [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]
    return pairs

print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))
