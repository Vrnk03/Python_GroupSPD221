class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.20462

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Килограммы должны быть числом')


obj = KgToPounds(10)
print(obj.kg)
obj.kg = 20   
print(obj.kg)
print(obj.to_pounds())
