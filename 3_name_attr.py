class Person:
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print(f'Hi I am.... {self.name}')


individual = Person('Sagar')
individual.talk()

john =Person('John')
john.talk()