
def get_number_of_frogs(year: int) -> int:
    count_frogs = 120
    caught_frogs = 50
    new_count_frog = (count_frogs - caught_frogs)*2
    res = (new_count_frog - count_frogs) * year + count_frogs
    return res

print(get_number_of_frogs(3))
