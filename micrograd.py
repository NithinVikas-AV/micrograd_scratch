import math
import numpy as np
import matplotlib.pyplot as plt
from graph import *

class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Valuedata(data={self.data}, children={self._prev}, op={self._op}, label={self.label})"
    
    def __add__(self, other):
        out = Value(self.data + other.data, (self.label, other.label), '+')
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out

a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = a+b; c.label='c'
print(c._prev)
