
#8.1
import itertools
val = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
suit = ['clubs', 'diamonds', 'hearts', 'spades']
deck = list(itertools.product(val, suit))
for val, suit in deck:
    print('%s of %s' % (val, suit))
print ()


#8.2
import itertools
import random
val = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
suit = ['clubs', 'diamonds', 'hearts', 'spades']
deck = list(itertools.product(val, suit))
random.shuffle(deck)
for val, suit in deck:
    print('%s of %s' % (val, suit))
print()


#8.3
class Car:
    def __init__(self, brand = "", reg = ""):
        self.brand = brand
        self.reg = reg

    def __str__(self):
        return self.brand + " " + self.reg + " "

    brand = ""
    reg = ""