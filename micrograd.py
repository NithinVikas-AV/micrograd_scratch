import math
import numpy as np
import matplotlib.pyplot as plt
from graph import *

class Value:

    def __init__(self, data, label=''):
        self.data = data
        self.label = label

    def __repr__(self):
        return f"Value( data = {self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data)
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data)
        return out

a = Value(5.0, 'a')
b = Value(4.0, 'b')

print(a )
print(b)

c = a + b; c.label = 'c'
d = a * b; d.label = 'd'

print(c)
print(d)