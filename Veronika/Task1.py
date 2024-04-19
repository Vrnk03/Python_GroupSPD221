class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.__age = age
        else:
            print('Invalid value')


u1 = User('Ivan', 10)
print(u1.get_name(), u1.get_age())
u1.set_age(12)
print(u1.get_name(), u1.get_age())
