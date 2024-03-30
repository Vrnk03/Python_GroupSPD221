"""
на соревнованиях по стрельбе участники получили следующие результаты:


Используя анонимную функцию, отсортировать результаты (словари) в порядке возрастания результата
"""
results = [
    {"name": "Avanov", "score": 95},
    {"name": "Betrov", "score": 92},
    {"name": "Sidorov", "score": 98},
    {"name": "Pavlov", "score": 99}
]

f = lambda x: x["name"]
print(sorted(results, key=f))
