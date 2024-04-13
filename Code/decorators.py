from time import time
from functools import wraps


def time_counter(unable=True):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            This is wrapper
            :param args:
            :param kwargs:
            :return:
            """
            if unable:
                start = time()
                result = func(*args, **kwargs)
                end = time() - start
                print("Execution time: ", end)
                return result
            else:
                result = func(*args, **kwargs)
                return result
        return wrapper
    return actual_decorator


# def time_counter(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time() - start
#         print("Execution time: ", end)
#         return result
#     return wrapper


@time_counter(unable=False)
def get_sum(n):
    """
    new function
    :param n:
    :return:
    """
    res_ = 0
    for i in range(n):
        res_ += i
    return res_

# r = get_sum(1000)
# res = time_counter(r)

res = get_sum(10000000)
# print(get_sum.__doc__)
print(res)