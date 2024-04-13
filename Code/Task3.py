"""
Сделаем класс Worker с атрибутами job, salary. salary - будет приватным.
Выполниить доступ к salary через геттер и сеттер
"""


# class Worker:
#     def __init__(self, job, salary):
#         self.job = job
#         self.__salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         self.__salary = value
#
#
# worker = Worker('teacher', 1000)
# print(worker.salary)
# worker.salary = 1500
# print(worker.salary)


class Worker:
    salary_map = {
        "A": 1500,
        "B": 1000,
        "C": 500
    }

    def __init__(self, worker_class):
        self.__salary = self.__get_salary(worker_class)

    @property
    def salary(self):
        return self.__salary

    def __get_salary(self, w_class: str) -> int:
        return self.salary_map.get(w_class, 0)


worker2 = Worker("D")
print(worker2.salary)
