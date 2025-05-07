import math
import numpy as np
import matplotlib.pyplot as plt
from graph import *

class Value:

    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self.grad = 0.0
        self.label = label

    def __repr__(self):
        return f"Value( data = {self.data}, children = {self._prev}, op = {self._op}, label = {self.label} )"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), _op = '+')
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), _op = '*')
        return out
    
    def tanh(self):
        x = self.data
        t = ((math.exp(2*x)-1)/(math.exp(2*x)+1))
        out = Value(t, (self, ), 'tanh')
        return out

# Inputs
x1 = Value(2.0, label='x1')
x2 = Value(0.0, label='x2')

# Weights
w1 = Value(-3.0, label='w1')
w2 = Value(1.0, label='w2')

#Bias
b = Value(6.8813735870195432, label='b')

# Weighted Sum
x1w1 = x1*w1; x1w1.label='x1w1'
x2w2 = x2*w2; x2w2.label='x2w2'
x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label='x1w1x2w2'
n = x1w1x2w2 + b; n.label='n'
o = n.tanh(); o.label='o'
o.grad = 1.0

# Gradients
n.grad = 1 - o.data**2
b.grad = 1 * n.grad
x1w1x2w2.grad = 1 * n.grad
x1w1.grad = x2w2.data * x1w1x2w2.grad
x2w2.grad = x1w1.data * x1w1x2w2.grad
x1.grad = w1.data * x1w1.grad
w2.grad = x1.data * x1w1.grad
x2.grad = w2.data * x2w2.grad
w2.grad = x2.data * x2w2.grad

dot = draw_dot(o)
dot.render('graph_output', format='png', view=True)