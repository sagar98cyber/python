#rolling a dice and returning tuples as a return value
import random

class Dice:
    def roll(self):
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        dice = (num1,num2)
        return dice

command = ''

print("""
'QUIT': Quit the game !!!
'ROLL': To roll the dice !!!
""")

dice = Dice()

while command.lower() != 'quit':
    command = str(input('> '))
    if command.lower() == 'roll':
        print(dice.roll())
        print()
    else:
        print('Kindly enter a Valid Input')