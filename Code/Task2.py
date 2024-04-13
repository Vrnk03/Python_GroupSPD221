"""
Создать класс car c атрибутами модель, объем двигателя и методами ride_forward, ride_backward
"""


class Car:
    def __init__(self, model, vol):
        self.model = model
        self.vol = vol

    def ride_forward(self):
        return f"{self.model} is riding forward"

    def ride_backward(self):
        return f"{self.model} is riding backward"


car1 = Car("car1", 6)
print(car1.ride_forward())