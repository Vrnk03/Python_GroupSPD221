"""
Модернизировать функцию обхода словаря так, чтобы она находила и суммиролвала
все значения списков.
Разрешается использовать дополнительные функции
"""


dct_data = {
    "a": "some_string",
    "b": {
        "c": "another_string",
        "d": [1, 2, 2, 4]
    },
    "e": {
        "a": [1, 2, 3]
    }
}


def find_obj(obj: dict):
    for key, val in obj.items():
        if isinstance(val, list):
            return sum(val)
        elif isinstance(val, dict):
            return find_obj(val)


print(find_obj(dct_data))