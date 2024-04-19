class Soda:
    def __init__(self, topping=''):
        self.topping = topping

    def show_my_drink(self):
        if(self.topping):
            print(f'Газировка с {self.topping}')
        else:
            print('Вода с газом')


s1 = Soda()
s1.show_my_drink()
s2 = Soda('яблоком')
s2.show_my_drink()

