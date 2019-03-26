#MSdie.py

import random
from random import randint
import numpy as np

random.seed(42)

class Die(object):


#constructor here
   def __init__(self):
       self.sides = 6
       self.roll()

#define classmethod 'roll' to roll the Die

   def roll (self):
       self.value = 1+random.randrange(self.sides)
       return self.value

#define classmethod 'getValue' to return the current value of the Die

   def getValue (self):
       return self.value

#define classmethod 'setValue' to set the die to a particular value

#def setValue (self,value):
   def setValue( self, value):
       return self.value

def main():
   d1 = Die()
   for n in range (6):
       print(d1.roll())
       print(d1.getValue())
       print(d1.setValue(8))

main()
