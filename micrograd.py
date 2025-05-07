import math
import numpy as np
import matplotlib.pyplot as plt
from graph import *

class Value:

    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self._prev = set(_children)
        self.label = label
        self._op = _op
        self.grad = 0.0
        self.back

    def __repr__(self):
        return f"Value( data = {self.data}, children = {self._prev}, op = {self._op}, label = {self.label} )"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), _op = '+')
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), _op = '*')

a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')
e = a*b; e.label='e'
d = e+c; d.label='d'
f = Value(-2.0, label='f')
L1 = d*f; L1.label='L1'
L1.grad = 1.0
print("L1: ",L1.data)

dot = draw_dot(L1)
dot.render('graph_output', format='png', view=True)