import math
import numpy as np
import matplotlib.pyplot as plt
from graph import *

class Value:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Value( data = {self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data)
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data)

a = Value(5.0)
b = Value(4.0)
c = a + b
print(c)