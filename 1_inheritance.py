class Mammal:
    def walk(self):
        print(f'Walk')     


class Dog(Mammal):
    def __init__(self):
        print('Bark!!')
        super().__init__()

    def nature(self):
        print('Friendly')


class Cat(Mammal):
    def __init__(self):
        print('Meow!!')
        super().__init__()

    def nature(self):
        print('Pridy')


pug = Dog()
fur = Cat()

pug.walk()
fur.nature()